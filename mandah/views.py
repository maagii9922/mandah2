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
    print(request.method)
    x=request.POST['name']
    y=request.POST['code']

    h=Hereglegch.objects.filter(name=x,code=y)
    
    return render(request,'login.html',{'aldaa':'aldaa garlaa','buruu':x,'buruu2':y})



    # print(len(h))
    # if len(h)==1: 
    #     # return HttpResponse('OK')
    #     b=Baraa.objects.all()
    #     return render(request,'home.html',{'user':h[0].name, 'baraa':b})
    # elif len(h)==0:
    #     # return HttpResponse('error')
    #     return render(request,'login.html',{'aldaa':'aldaa garlaa','buruu':x,'buruu2':y})

        
    # return HttpResponse('server error')