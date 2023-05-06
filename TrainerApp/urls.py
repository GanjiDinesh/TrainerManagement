from django.urls import path

from TrainerApp import views

urlpatterns = [
    path('',views.home),
    path('adminhome',views.adminhome,name='adminhome'),
    path('trainerhome',views.trainerhome,name='trainerhome'),
    path('register', views.register_fun, name='register'),
    path('readregister', views.register_read, name='readregister'),
    path('login',views.login_fun,name='login'),
    path('readlogin',views.login_read,name='readlogin'),
    path('trainerdetails',views.trainerdetails,name='trainerdetails'),
    path('batchassign',views.batchassign,name='batchassign'),
    path('readbatchassign',views.readbatchassign,name='readbatchassign'),
    path('batchdetails',views.batchdetails,name='batchdetails'),
    path('trainerbatchdetails',views.trainerbatchdetails,name='trainerbatchdetails'),
    path('logout',views.logout_fun,name='logout')
]