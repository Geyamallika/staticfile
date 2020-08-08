from django.shortcuts import render
from django.http import HttpResponse

def trial(request):
    return HttpResponse("<h1>Project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"myapp/home.html")

def profile(request):
    name="akshay"
    return render(request,"myapp/profile.html",{'name':name})

