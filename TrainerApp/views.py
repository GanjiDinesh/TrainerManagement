from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from TrainerApp.models import City, Course, Trainer, BatchAssign


# Create your views here.
def home(request):
    return redirect('login')

def adminhome(request):
    return render(request,'adminhome.html')

def trainerhome(request):
    return render(request,'trainerhome.html')

def register_fun(request):
    cities = City.objects.all()
    course = Course.objects.all()
    return render(request, 'register.html', {'cities': cities, 'course': course})


def register_read(request):
    t = Trainer()
    usertype = request.POST['usertype']
    if usertype == "Admin":
        uname = request.POST['tbusername']
        email = request.POST['tbemail']
        password = request.POST['tbpass']
        user = User.objects.create_superuser(username=uname, email=email, password=password)
        user.save()
        return render(request, 'login.html', {'name': user, 'msg': f'user created successfully username is '})
    else:
        t.trainer_name = request.POST['tbusername']
        t.email = request.POST['tbemail']
        t.phoneno = request.POST['tbphno']
        t.password = request.POST['tbpass']
        t.city = City.objects.get(city_name=request.POST['ddlcity'])
        t.course = Course.objects.get(course_name=request.POST['ddlcourse'])
        t.save()
        return render(request,'login.html')


def login_fun(request):
    return render(request, 'login.html')


def login_read(request):
    uname = request.POST['tbusername']
    password = request.POST['tbpass']
    usertype = request.POST['usertype']
    myuser = authenticate(username=uname, password=password)
    if myuser is not None and usertype == "Admin":
        login(request, myuser)
        return render(request,'adminhome.html')
    elif Trainer.objects.filter(Q(trainer_name=uname) & Q(password=password)).values():
        return render(request,'trainerhome.html')
    else:
        return render(request, 'login.html')


def trainerdetails(request):
    return render(request,'trainerdetails.html',{'trainer':Trainer.objects.all()})


def batchassign(request):
    trainerid = Trainer.objects.all()
    course = Course.objects.all()
    return render(request,'batchassign.html',{'trainerid':trainerid,'course':course})


def readbatchassign(request):
    b = BatchAssign()
    b.trainer_id = Trainer.objects.get(id=request.POST['ddltrainerid'])
    b.date_time = request.POST['tbdate']
    b.classroom = request.POST['tbclassroom']
    b.course = Course.objects.get(course_name=request.POST['ddlcourse'])
    b.batch_no = request.POST['tbbatchno']
    b.save()
    b = BatchAssign.objects.all()
    return render(request,'batchdetails.html',{'data':b})

def batchdetails(request):
    return render(request,'batchdetails.html',{'data':BatchAssign.objects.all()})

def trainerbatchdetails(request):
    return render(request,'trainerbatchdetails.html',{'data':BatchAssign.objects.all()})

def logout_fun(request):
    logout(request)
    return redirect('login')

