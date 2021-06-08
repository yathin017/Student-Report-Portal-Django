from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact, Student
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User, auth



class Sum:
    def __init__(self,SITW,SIOT,SS,SClang):
        self.SITW=SITW
        self.SIOT=SIOT
        self.SS=SS
        self.SClang=SClang
        self.Perc=(SClang+SIOT+SS+SITW)/400*100
        self.GPA=self.Perc/9.5*100


# Create your views here.

def home(request):
    return render(request,'home.html')

def graph(request):
    return render(request,'graph.html')

def result(request):
    global stud
    x=int(request.POST['username'])
    stud=Student.objects.get(roll_number=x)
    return render(request,'result.html',{'stu':stud})

def login(request):
        if request.method == "POST":
            username = request.POST['username']
            #password = request.POST['password']
            user = auth.authenticate(username=username)
            if user is not None:
                auth.login(request,user)
                stud=Student.objects.filter(roll_number=request.username)
                return redirect(request,"result",{'stu':stud})
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('login')
        else: 
            return render(request,'login.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        prob = request.POST.get('prob')
        contact = Contact(name=name, email=email, prob=prob, date=datetime.today())
        contact.save()
        messages.success(request,"Your message has been sent!!!")
    return render(request,'contact.html')

def logout(request):
    messages.info(request,"Session Logged Out")
    return redirect('login')