from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'home.html',{'name':'praneeth kumar'})
def add(req):
    val1=int(req.POST['num1'])
    val2=int(req.POST['num2'])
    res=val1+val2
    return render(req,'result.html',{'result':res})