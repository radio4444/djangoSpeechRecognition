from django import forms
from .models import UserInfo


#  forms are a fundamental component used to handle user input and interact with data.
class UserForm(forms.ModelForm):
	class Meta:
		model = UserInfo
		fields = ['name', 'email', 'address', 'phone_number']
