from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm

# Create your views here.

def registerUser(request):
   # return HttpResponse('This is a user reg form') Commented in Ch33
   #Ch 34

   if request.method =='POST':
      print(request.POST)
   else:      
      form=UserForm()
   context={
      'form':form
   }
   return render(request,'accounts/registerUser.html')
