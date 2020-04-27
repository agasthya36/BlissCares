from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views import View
from .models import Appointment
from .models import Doctors,Comment
from .models import Consultation,Post
from django.contrib.auth.models import User

from .forms import Signup,comment
from .forms import book
from django.contrib.auth.decorators import login_required
def home(request):
	return render(request,"appointment/home.html")
@login_required(login_url="loginuser")
def home1(request):
	return render(request,"appointment/home1.html")


@login_required(login_url="loginuser")
def deleteappointment(request):
	f=""
	n=request.user.username
	print(n)
	if request.method=='POST':
		appointment_id =request.POST.get('id')
		a=Consultation.objects.filter(appointment_id=int(appointment_id))
		
		for i in a:
			f=i.username
			break
		print(f)
		
		
		
		b=Consultation.objects.values_list("appointment_id",flat=True)
		
		

		if (int(appointment_id) not in b) or (f!=request.user.username):
			messages.info(request,"enter a valid appointment id")
			return redirect("deleteappointment")


		else:

			a=a.delete()
			messages.info(request,"Appointment deleted")
			return redirect('deleteappointment')



	return render(request,"appointment/a.html")
def signup(request):
	form=Signup()
	if request.method=='POST':
		form=Signup(request.POST)
		if(form.is_valid()):
			form.save()
			return redirect("loginuser")
	return render(request,"appointment/register.html",{'form':form})
def loginuser(request):
	print(request.user.username)

	if request.method=="POST":
		username=request.POST.get("username")
		password=request.POST.get("password")
		a=authenticate(request,username=username,password=password)
		if a is not None:
			login(request,a)
			return redirect("home1")
		else:
			messages.info(request,"username or password is incorect")
	return render(request,"appointment/login.html")

def logoutuser(request):
	for i in list(request.session.keys()):
		del request.session[i]		
	logout(request)
	return redirect("loginuser")

@login_required(login_url="loginuser")
def book_appointment(request):
	form=book()
	if request.method=="POST":
		form=book(request.POST)
		if(form.is_valid()):
			date1=request.POST.get('date')
			specialist1=request.POST.get('specialist')
			name=request.POST.get('name')
			request.session['date']=date1
			request.session['specialist']=specialist1
			request.session['name']=name




			form.save()

			return redirect("doctor_name")
			
	return render(request,"appointment/bookappointment.html",{'form':form})

@login_required(login_url="loginuser")
def doctor_name(request):
	specialist=request.session['specialist']
	dnames=[]
	dname=Doctors.objects.filter(specialist=specialist)
	for i in dname:
		if i.name not  in dnames:
			dnames.append(i.name)
	if request.method=="POST": 
		doctor=request.POST.get('doctor')
		print(doctor)
		if doctor==None:
			messages.info(request,"please select a doctor")
			return redirect("doctor_name")
		else:
			request.session['doctor']=doctor

			
			return redirect("book_appointment1")

	
	return render(request,"appointment/selectdoctor.html",{"dnames":dnames})
@login_required(login_url="loginuser")
def book_appointment1(request):	
	date1=request.session['date']
	print(date1)
	doctor1=request.session['doctor']
	
	specialist1=request.session['specialist']
	d1=Doctors.objects.filter(specialist=specialist1,name=doctor1)
	f=Consultation.objects.filter(appointment_date=date1,doctor=doctor1)
	hospital_list={}
	t2=[]
	time3=[]
	count=0 
	for i in d1:
		h=i.hospital
		
		a,b=i.available_time1.split("-")
		for j in f:
	 		if j.hospital==h:
	 			t2.append(str(j.time))
		print(t2)
	 		
		i=int(a)
		while(i!=int(b)):
	 		c=i
	 		if count%2==0:
	 			if i<=9:
	 				i=str(0)+str(i)+":"+"00"+":"+"00"
	 			else:
	 				i=str(i)+":"+"00"+":"+"00"

	 			
	 		else:
	 			if i<=9:
	 				i=str(0)+str(i)+":"+"30"+":"+"00"
	 			else:
	 				i=str(i)+":"+"30"+":"+"00"

	 		if i not in t2:
	 			time3.append(i)
	 		
	 		if count%2==0:
	 	 		i=c
	 		else:
	 			i=c+1
	 		count=count+1
		hospital_list[h]=time3
		time3=[]
	 		
	doctor_timing=filter(None,time3)
	print(hospital_list)
	if request.method=="POST":
		selected_hospital=request.POST.get('selected_hospital')
		time_slot=request.POST.get('time')
		if selected_hospital is None:
			messages.info(request,"select a hospital")
		elif time_slot is None:
			messages.info(request,"select time")
		elif selected_hospital and time_slot is None:
			messages.info(request,"select hospital and time")
		else:
			request.session['selected_hospital']=selected_hospital
			request.session['time_slot']=time_slot

			return redirect("booked_appointment")

	return render(request,"appointment/bookappointment1.html",{"hospital_list":hospital_list})	
@login_required(login_url="loginuser")

def booked_appointment(request):
	c=0
	n=request.user.username
	
	id1=(Consultation.objects.values_list("appointment_id",flat=True))
	print(id1)
	if not id1:
		c=1
	else:
		c=max(id1)+1
	appointment=Consultation()
	appointment.username=n
	appointment.appointment_id=c
	appointment.name=request.session['name']
	appointment.doctor=request.session['doctor']
	appointment.hospital=request.session['selected_hospital']
	appointment.appointment_date=request.session['date']
	appointment.time=request.session['time_slot']
	appointment.save()
	print(appointment.name,appointment.doctor,appointment.hospital,appointment.appointment_date,appointment.time)
	return render(request,"appointment/bookappointment2.html",{"appointment":appointment})
@login_required(login_url="loginuser")
def posttitles(request):
	post_list=Post.objects.all()
	
	
	return render(request,"appointment/post_list.html",{"post_list":post_list})
from .forms import post
@login_required(login_url="loginuser")
def addpost(request):
	form=post()

	if request.method=="POST":
		form=post(request.POST)
		if form.is_valid():
			form.save()
			return redirect("posttitles")
	return render(request,"appointment/addpost.html",{"form":form})



@login_required(login_url="loginuser")
def postdetails(request,pk):
	c1=[]
	p=Post.objects.get(pk=pk)
	c=Post.objects.filter(title=p)
	d=Comment.objects.filter(topic=p)
	for i in d:
		c1.append(i.text)
	e=Post.objects.filter(title=p).first()
	print(e)
	f=e.post_comments()
	u=request.user.username
		
	

	
	form = comment(initial={'topic': Post.objects.get(pk=pk),'commenter':User.objects.get(username=u)})

	
	if request.method=="POST" and "submit5" in request.POST:
		form=comment(request.POST)
		if(form.is_valid()):
			i=form.save(commit=False)
			try:
				t=Post.objects.get(id=pk)
				user1=User.objects.get(username=u)
				print(user1)


			except Post.DoesNotExist:
				pass
			i.topic=t
			i.commenter=user1

			i.save()

			return redirect("posttitles")

		

	
	return render(request,"appointment/post_detail.html",{"c1":c1,"form":form,"comment":comment,"e":f,"p":p})

