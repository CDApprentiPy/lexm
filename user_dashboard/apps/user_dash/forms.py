from django import forms
from django.core.validators import validate_email

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class Register(forms.Form):
    # def __init__(self, *args, **kwargs):
    #     super(Register, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()

    first_name = forms.CharField(label="First Name:", max_length=45, min_length=2)
    last_name = forms.CharField(label="Last Name:", max_length=45, min_length=2)
    email = forms.CharField(label="Email:", max_length=255, validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),label="Password:", max_length=258, min_length=8)
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),label="Confirm pw:", max_length=255, min_length=8)
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/process'
    helper.add_input(Submit('submit', 'Register'))

class Login(forms.Form):
    email = forms.CharField(label="Email:", max_length=255, validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),label="Password:", max_length=255, min_length=8)

    helper = FormHelper()
    helper.form_class = 'form-horizontal'
