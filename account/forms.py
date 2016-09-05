from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# User Registration
class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match')
		return cd['password2']

"""
	This check is done when we validate the form calling its is_valid() method,
	You can provide a clean_<fieldname>() method to any of your form fields in
	order to clean the value or raise form validation erros for specific fields

	Forms also includes a general clean() method to validate the entire form, which
	is useful to validate fields that depend on each other.

	Django also provides a UserCreationForm that reside in django.contrib.auth.forms
"""