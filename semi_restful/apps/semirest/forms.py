from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=255)
    last_name = forms.CharField(label="Last Name", max_length=255)
    email = forms.CharField(label="Email", max_length=255)
