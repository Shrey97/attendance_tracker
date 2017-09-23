from django import forms
from .models import student,prof,course,attn

class ProfileForm(forms.ModelForm):

    class Meta:
        model = student
        fields = ('name', 'roll','year','email','department', 'photo')
