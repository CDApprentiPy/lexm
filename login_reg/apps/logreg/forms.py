from django import forms
from django.core.validators import validate_email

class Register(forms.Form):
    first_name = forms.CharField(label="First Name:", max_length=45, min_length=2)
    last_name = forms.CharField(label="Last Name:", max_length=45, min_length=2)
    email = forms.CharField(label="Email:", max_length=255, validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),label="Password:", max_length=258, min_length=8)
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),label="Confirm pw:", max_length=255, min_length=8)
    def clean(self):
        # cleaned_data = super(Register, self).clean()
        password = self.cleaned_data.get('password')
        confirm = self.cleaned_data.get('confirm')
        if password and confirm and password != confirm:
            raise forms.ValidationError("Passwords do not match!")
        return self.cleaned_data

class Login(forms.Form):
    email = forms.CharField(label="Email:", max_length=255, validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),label="Password:", max_length=255, min_length=8)
