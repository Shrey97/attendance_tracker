from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
@login_required
def profile(request):
    if(request.user.groups.filter(name='Students').exists()):
        print(student.objects.filter(useri=request.user))
        us = student.objects.filter(useri = request.user)[0]
        # name = request.user
        print(us.id)
        print(us)
        all_courses = course.objects.all()
        atten = attn.objects.filter(student = us)
        # print(atten, atten.ATT, atten.course)
        attlist = []
        for i in range(len(all_courses)):
            c = all_courses[i]
            at = atten.filter(course=c)[0].ATT
            attlist.append((all_courses[i], at))
        return render(request, 'showprofile.html', {'us':us, 'attlist' : attlist, 'roll':us.roll})
    elif(request.user.groups.filter(name='professors').exists()):
        pp = prof.objects.filter(useri=request.user)[0]
        return render(request, 'profprofile.html', {'pp':pp})

class StudentUpdate(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
        permission_required = ["student.is_student"]
        model = student
        fields = ['name', 'department', 'email', 'photo', 'year', 'roll']

@permission_required('attd.is_prof')
@login_required
def mark_attn(request):
    list_of_students = student.objects.all()
    pr = prof.objects.filter(name = User.first_name)
    return render(request, 'markatt.html', {'list':list_of_students})

@permission_required('attd.is_prof')
@login_required
def mark_att_st(request, roll):
    stud = student.objects.get(roll = roll)
    print(stud)
    pr = prof.objects.filter(useri=request.user)
    print(pr)
    if(pr):
        cou = pr[0].course
        a = attn.objects.filter(course=cou).filter(student=stud)[0]
        print(a)
        a.ATT += 1
        a.save()

    return HttpResponse("attendance marked!")

@login_required
def edit_profile(request):
    us = student.objects.filter(useri=request.user)
    post = get_object_or_404(student, useri=request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/accounts/profile')
    else:
        form = ProfileForm(instance=post)
    return render(request, 'edit_profile.html', {'form': form, 'us':us[0]})

@permission_required('attd.is_prof')
@login_required
def attendance_done(request):
    pr = prof.objects.filter(useri = request.user)
    c = pr[0].course
    x = request.POST.getlist('present[]')
    n = len(x)
    for i in x:
        s = student.objects.filter(roll = i)[0]
        at = attn.objects.filter(student = s).filter(course = c)[0]
        at.ATT += 1
        at.save()
    return render(request, 'thanksforatt.html', {'n':n, 'pp':pr[0]})
