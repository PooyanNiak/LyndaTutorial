from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput)
    
class RegisterForm(forms.Form):
	username = forms.CharField(min_length=4, max_length=32)
	password = forms.CharField(widget=forms.PasswordInput)
	confirmPassword = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField()
	age = forms.IntegerField(min_value=6, max_value=100)