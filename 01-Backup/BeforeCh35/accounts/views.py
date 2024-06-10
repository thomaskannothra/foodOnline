from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .models import User

from .forms import UserForm

# Create your views here.

def registerUser(request):
   # return HttpResponse('This is a user reg form') Commented in Ch33
   #Ch 34

   if request.method =='POST':
      print(request.POST)
      form=UserForm(request.POST)
      if  form.is_valid():
         #form.save()
         user=form.save(commit=False)
         user.role=User.CUSTOMER
         #Above line adds customer for the role field
         user.phone_number= "123"
         user.save()         
         return redirect('registerUser')
      else:
         print(form.errors)
   else:      
      form=UserForm()
   context = {
      'form': form,
   }
   return render(request,'accounts/registerUser.html',context)
