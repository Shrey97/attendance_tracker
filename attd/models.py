from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class student(models.Model):
    useri = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll = models.IntegerField(default=0)
    year = models.IntegerField(default=2017)
    email = models.EmailField(blank = True, null = True)
    DEP = (
        ('Computer Science', 'Computer Science'),
        ('Mechanical', 'Mechanical'),
        ('Mathematics', 'Mathematics'),
    )
    department = models.CharField(max_length=100, choices = DEP, null = True, help_text = "department")
    photo = models.FileField(blank=True, upload_to='images/')

    # at = models.ManyToManyField('attn')
    def __str__(self):
        return str(self.name)

    class Meta:
        permissions = (("is_student", "is_student"), )

    def get_absolute_url(self):
        return reverse('profile')

class prof(models.Model):
    useri = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    course = models.ForeignKey('course', on_delete=models.SET_NULL, null=True)
    photo = models.FileField(null=True, upload_to='images/')
    class Meta:
        permissions = (("is_prof", "is_prof"), )

    def __str__(self):
        return str(self.name)

class course(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)

class attn(models.Model):
    student = models.ForeignKey(student, on_delete=models.SET(0))
    course = models.ForeignKey(course, on_delete=models.SET(0))
    ATT = models.IntegerField(default=0, null=True)

    def __str__(self):
        return str(self.course) + " " + str(self.student.roll)
