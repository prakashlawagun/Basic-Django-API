from django import forms
from .models import User


class EmployeeRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'address', 'phone']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),

        }
