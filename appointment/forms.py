# from .models import appointment
from django import forms
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Appointment
from .models import Post,Comment


class Signup(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email','password1','password2']
class book(forms.ModelForm):
	# appointment_date= DateTimeField(widget = DateInput(format='%Y-%m-%d'),
 #                                   input_formats=('%Y-%m-%d',),
 #                                   required=False)
	class Meta:
		
		model=Appointment
		fields=("name","contact_no","specialist","date")
		widgets={
			'date':forms.TextInput(attrs={'placeholder':'yyyy-mm-dd'})
		}
class post(forms.ModelForm):
	class Meta:
		model=Post
		fields=("title","description")

class comment(forms.ModelForm):
	class Meta:
		model=Comment
		widgets={
			'text':forms.Textarea(attrs={'cols':150,'rows':5})
		}
		
		fields=('topic','commenter','text','vote',)
		

		
