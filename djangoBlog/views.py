from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')

    # return HttpResponse('home')

# def sst(request):
    # return HttpResponse ('avalbad')
