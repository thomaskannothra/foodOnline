from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   # return HttpResponse('TMK')
   return render(request,'home.html')