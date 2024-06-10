from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .models import User

from .forms import UserForm
import random

# Create your views here.

def registerUser(request):
   # return HttpResponse('This is a user reg form') Commented in Ch33
   #Ch 34

   if request.method =='POST':
      print(request.POST)
      form=UserForm(request.POST)
      if  form.is_valid():
         #form.save()
         # MEthod 1 -HasH
         #password= form.cleaned_data['password'] #Ch35
         #user=form.save(commit=False)
         #user.set_password(password)#Ch35
         #user.role=User.CUSTOMER
         ##Above line adds customer for the role field
         #user.phone_number= random.Random()
         #user.save()       
         first_name= form.cleaned_data['first_name']
         last_name= form.cleaned_data['last_name']
         username=form.cleaned_data['username']
         email=form.cleaned_data['email']
        # phone_number=form.cleaned_data['phone_number']
         password=form.cleaned_data['password']
         
         
         user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                       email=email,password=password)
         user.role=User.CUSTOMER
         user.save()
         print('User is created')
         # Create user using Create_user  Method
         return redirect('registerUser')
      else:
         print(form.errors)
   else:      
      form=UserForm()
   context = {
      'form': form,
   }
   return render(request,'accounts/registerUser.html',context)
