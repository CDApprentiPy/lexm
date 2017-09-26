from django import forms
from django.core.validators import validate_email

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field, Fieldset, ButtonHolder
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class Register(forms.Form):
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
    def clean(self):
        form_data = self.cleaned_data
        print "form_data", form_data
        if form_data.get('password') != form_data.get('confirm'):
            msg = 'Passwords do not match!'
            self.add_error('password', msg)
        return form_data

class NewUser(forms.Form):
    first_name = forms.CharField(label="First Name:", max_length=45, min_length=2)
    last_name = forms.CharField(label="Last Name:", max_length=45, min_length=2)
    email = forms.CharField(label="Email:", max_length=255, validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),label="Password:", max_length=258, min_length=8)
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),label="Confirm pw:", max_length=255, min_length=8)
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/process'
    helper.add_input(Submit('submit', 'Create'))
    def clean(self):
        form_data = self.cleaned_data
        print "form_data", form_data
        if form_data.get('password') != form_data.get('confirm'):
            msg = 'Passwords do not match!'
            self.add_error('password', msg)
        return form_data

class Login(forms.Form):
    email = forms.CharField(label="Email:", max_length=255, validators=[validate_email])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),label="Password:", max_length=255, min_length=8)
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/login'
    helper.add_input(Submit('submit', 'Sign In'))

class EditUser(forms.Form):
    def __init__(self,*args,**kwargs):
        self.mail = kwargs.pop('mail')
        self.fname = kwargs.pop('fname')
        self.lname = kwargs.pop('lname')
        super(EditUser,self).__init__(*args,**kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'value':self.mail})
        self.fields['first_name'].widget = forms.TextInput(attrs={'value':self.fname})
        self.fields['last_name'].widget = forms.TextInput(attrs={'value':self.lname})
    email = forms.CharField(label="Email Address:", max_length=255, validators=[validate_email])
    first_name = forms.CharField(label="First Name:", max_length=45, min_length=2)
    last_name = forms.CharField(label="Last Name:", max_length=45, min_length=2)
    helper = FormHelper()
    helper.layout = Layout(
        Fieldset(
            'Edit Information',
            Field('email'),
            Field('first_name'),
            Field('last_name'),
        ),
        ButtonHolder(
            Submit('submit', 'Save'),
        )
    )
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/update'


class EditUserAdmin(forms.Form):
    def __init__(self,*args,**kwargs):
        self.mail = kwargs.pop('mail')
        self.fname = kwargs.pop('fname')
        self.lname = kwargs.pop('lname')
        self.level = kwargs.pop('level')
        super(EditUserAdmin,self).__init__(*args,**kwargs)
        self.fields['email'].widget = forms.TextInput(attrs={'value':self.mail})
        self.fields['first_name'].widget = forms.TextInput(attrs={'value':self.fname})
        self.fields['last_name'].widget = forms.TextInput(attrs={'value':self.lname})
        self.fields['user_level'].initial = self.level
    USER_TYPES = (
        (1, 'Normal'),
        (9, 'Admin'),
    )
    email = forms.CharField(label="Email Address:", max_length=255, validators=[validate_email])
    first_name = forms.CharField(label="First Name:", max_length=45, min_length=2)
    last_name = forms.CharField(label="Last Name:", max_length=45, min_length=2)
    user_level = forms.ChoiceField(label="User Level:", choices=USER_TYPES)
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/update_admin'
    helper.add_input(Submit('submit', 'Save'))

class ChangePass(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),label="Password:", max_length=258, min_length=8)
    confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),label="Password Confirmation:", max_length=255, min_length=8)
    helper = FormHelper()
    helper.layout = Layout(
        Fieldset(
            'Change Password',
            Field('password'),
            Field('confirm'),
        ),
        ButtonHolder(
            Submit('submit', 'Update Password'),
        )
    )
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/change_pass'
    def clean(self):
        form_data = self.cleaned_data
        print "form_data", form_data
        if form_data.get('password') != form_data.get('confirm'):
            msg = 'Passwords do not match!'
            self.add_error('password', msg)
        return form_data


class EditDescription(forms.Form):
    def __init__(self,*args,**kwargs):
        self.desc = kwargs.pop('desc')
        super(EditDescription,self).__init__(*args,**kwargs)
        self.fields['description'].widget = forms.Textarea()
        self.fields['description'].initial = self.desc
    description = forms.CharField(label="Edit Description", max_length=1000)
    helper = FormHelper()
    helper.layout = Layout(
        Fieldset(
            'Edit Description',
            Field('description'),
        ),
        ButtonHolder(
            Submit('submit', 'Save'),
        )
    )
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'
    helper.form_action = '/edit_desc'
