# users/forms.py
from django import forms
from .models import UserProfile


class ProfileForm(forms.ModelForm):
    '''从模型继承表单'''
    class Meta:
        model = UserProfile
        fields = ['photo', 'gender', 'job', 'email', 'address']
