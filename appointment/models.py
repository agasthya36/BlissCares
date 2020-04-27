from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
#from django import models
from django import forms
from django.core.validators import MinLengthValidator

# Create your models here.
# class Appointment(models.Model):
choice=[("general","general"),("neurologist","neurologist"),("cardiologist","cardiologist"),("dermatologist","dermatologist"),("pediatrician","pediatrician"),
("psychiatrist","psychiatrist"),("orthopedician","orthopedician")]
class Appointment(models.Model):
	name=models.CharField(max_length=50)
	contact_no=models.CharField(validators=[MinLengthValidator(10)],max_length=10)
	#type1=models.CharField(max_length=50,choices=choice,default="general")
	specialist=models.CharField(max_length=50,blank=True,choices=choice,default='general')
	date=models.DateField(help_text='appointment_date')
	
class Doctors(models.Model):
	name=models.CharField(max_length=50)
	specialist=models.CharField(max_length=50)
	hospital=models.CharField(max_length=100)
	available_time1=models.CharField(max_length=50)

class Consultation(models.Model):
	username=models.CharField(max_length=50)
	appointment_id=models.IntegerField(null=True)
	name=models.CharField(max_length=50)
	doctor=models.CharField(max_length=50)
	hospital=models.CharField(max_length=50)
	appointment_date=models.DateField()
	time=models.TimeField()
vote_choice=[("u","upvote"),("d","downvote")]
class Post(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(blank=True, default='')
    created = models.DateTimeField(default=timezone.now)
    creator = models.ForeignKey(User, blank=True, null=True,on_delete=models.CASCADE)
    vote=models.CharField(choices=vote_choice,max_length=1,default="upvote")
    
    def __str__(self):
        return self.title
    def post_comments(self):
        comments=Comment.objects.filter(topic=self)

        return comments

    def no_likes(self):
        return self.vote.filter(type="u").count()
    def no_dislikes(self):
            return self.vote.filter(type="d").count()

class Comment(models.Model):
    text=models.TextField(blank=True)
    commenter=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    topic=models.ForeignKey(Post,on_delete=models.CASCADE,null=True,blank=True)
    vote=models.CharField(choices=vote_choice,max_length=1,null=True,blank=True)
    def no_likes(self):
        return self.vote.filter(type="u").count()
    def no_dislikes(self):
        return self.vote.filter(type="d").count()
