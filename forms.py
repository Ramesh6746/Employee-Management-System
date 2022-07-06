from django import forms
from django.forms import fields
from .models import Emp
from django.core import validators

class employeeregi(forms.ModelForm):
    class Meta:
        model = Emp
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }
