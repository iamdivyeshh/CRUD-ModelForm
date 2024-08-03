from django.core import validators
from django import forms
from .models import Students

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'city', 'number', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'city': forms.TextInput(attrs={'class': 'form-control','placeholder': 'City'}),
            'number': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control','placeholder': 'Password'}),
        }