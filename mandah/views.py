from django.http import HttpResponse
from django.shortcuts import render
from .models import Hereglegch

def index(request):
	return HttpResponse("welcome")

def home(request):
    return render(request,'home.html')


def home(request):
	h=Hereglegch.objects.all()
	return render(request,'home.html',{'hereglegch':h})