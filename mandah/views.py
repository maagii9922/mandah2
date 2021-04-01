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

def login(request):
    return render(request,'login.html')

def shalgah(request):
    # h=Hereglegch.objects.all()
    # return render(request,'home.html',{'hereglegch':h})
    print(request.method)
    x=request.POST['name']
    y=request.POST['code']
    # print(y)

    h=Hereglegch.objects.filter(name=x,code=y)
        

    print(len(h))
    if len(h)==1: 
        return render(request,'home.html',{'user':h[0].name})
    elif len(h)==0:
        # return HttpResponse('error')
        return render(request,'login.html',{'aldaa':'aldaa garlaa','buruu':x,'buruu2':y})
        
    return HttpResponse('server error')