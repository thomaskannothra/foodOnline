from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .models import User, UserProfile
from .forms import UserForm
from vendor.forms import VendorForm
import random

from django.contrib import messages # cH 37

# Create your views here.

def registerUser(request):
   # return HttpResponse('This is a user reg form') Commented in Ch33
   #Ch 34

   if request.method =='POST':
      #print(request.POST)
      form=UserForm(request.POST)
      if  form.is_valid():
         #form.save()
         # MEthod 1 -HasH
         password= form.cleaned_data['password'] #Ch35
         user=form.save(commit=False)
         user.set_password(password)#Ch35
         user.role=User.CUSTOMER
         #Above line adds customer for the role field
         user.phone_number= random.Random()
         user.save()       
         
         #Method 2 
         #first_name= form.cleaned_data['first_name']
        # last_name= form.cleaned_data['last_name']
        # username=form.cleaned_data['username']
        # email=form.cleaned_data['email']
        # phone_number=form.cleaned_data['phone_number']
        # password=form.cleaned_data['password']         
         
        # user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
        #                              email=email,password=password)
        # user.role=User.CUSTOMER
         #user.save()
        # print('User is created')
         # Create user using Create_user  Method
         
         messages.success(request,'Your account has been registered sucessfully-Views.py ')
         return redirect('registerUser')
      else:
         #print ('Invalid Form')
         print(form.errors)
   else:      
      form=UserForm()
   context = {
      'form': form,
   }
   return render(request,'accounts/registerUser.html',context)


def registerVendor(request):
   #Ch 43
   if request.method=='POST':
      # Store the data and cretae the user
      form=UserForm(request.POST)
      v_form=VendorForm(request.POST,request.FILES)
      if form.is_valid() and v_form.is_valid():
         first_name= form.cleaned_data['first_name']
         last_name= form.cleaned_data['last_name']
         username=form.cleaned_data['username']
         email=form.cleaned_data['email']         
         password=form.cleaned_data['password']   
         user=User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                      email=email,password=password)
         user.role=User.VENDOR
         user.save()   
         vendor=v_form.save(commit=False)
         vendor.user=user
         user_profile=UserProfile.objects.get(user=user)
         vendor.user_profile= user_profile
         vendor.save()
         messages.success(request,'Your account has been registred sucessfully! pls wait for the approval')
         return redirect('registerVendor')
   else:   
      form = UserForm()
      v_form=VendorForm()
   
   context={
      'form': form,
      'v_form':v_form,
   }
   return render(request,'accounts/registerVendor.html',context)
