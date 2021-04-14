from django.shortcuts import render , redirect
from .models import UserRegisterModel
from .forms import UserRegisterForm
from django.contrib.auth import get_user_model
from django.contrib import messages


from django.views.generic.edit import FormView
#mail
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login

# Create your views here.
def UserRegisterView(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['Name']
            dob=form.cleaned_data['DOB']
            email=form.cleaned_data['Email']
            print(email)
            Phone_number=form.cleaned_data['Phone_number']
            reg = UserRegisterModel(Name=nm , DOB= dob, Email=email, Phone_number=Phone_number)
           
    #    gmail verification logic        
            send_mail(
                'hi ! you are to close to submission',
                'please click on link ' 
                'http://127.0.0.1:8000/detail/',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            reg.save()
            message=messages.info(request, 'An confirmation link send on your gmail , check !!!')
    else:
        request.method == 'GET'
        form=UserRegisterForm()    
    return render(request,'app/userregister.html',{'form':form})

def allusers(request):
    data = UserRegisterModel.objects.all()
    return render(request,'app/allusers.html',{'data':data})   

