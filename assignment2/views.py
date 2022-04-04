from django.http import HttpRequest
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def entertainment(request):
    return render(request,"entertainment.html")

def event(request):
    return render(request,"events.html")