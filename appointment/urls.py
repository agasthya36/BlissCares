from django.urls import path,include
from .import views
urlpatterns=[
path('signup/',views.signup,name="signup"),
path('login',views.loginuser,name="loginuser"),
path('logout',views.logoutuser,name="logoutuser"),
path('delappointment',views.deleteappointment,name="deleteappointment"),
path('appointment',views.book_appointment,name="book_appointment"),
path('doctor',views.doctor_name,name="doctor_name"),
path("appointment1",views.book_appointment1,name="book_appointment1"),
path("appointment2",views.booked_appointment,name="booked_appointment"),
path("posttitle",views.posttitles,name="posttitles"),
path('postdetails/<pk>',views.postdetails,name="postdetails"),
path('',views.home,name="home"),
path('home1',views.home1,name="home1"),
path('addpost',views.addpost,name="addpost")]