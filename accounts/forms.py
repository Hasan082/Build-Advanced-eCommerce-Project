from django import forms
from .models import Account


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'email', 'phone', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'phone': 'Phone',
        }
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            if field in placeholders:
                self.fields[field].widget.attrs.update({'placeholder': placeholders[field]})
