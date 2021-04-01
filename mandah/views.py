from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse("welcome")

def home(request):
    return render(request,'home.html')