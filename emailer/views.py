from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.core.mail import send_mail, EmailMessage, get_connection
from django.conf import settings
import re

# Create your views here.


def home(request):
    return render(request, 'index.html')

def email(request):
    email = request.POST['email']
    email.strip()
    emailCheck = re.findall('@',email)
    if emailCheck:
       name = email.split('@')[0]
       with get_connection(  
           host=settings.EMAIL_HOST, 
           port=settings.EMAIL_PORT,  
           username=settings.EMAIL_HOST_USER, 
           password=settings.EMAIL_HOST_PASSWORD, 
           use_tls=settings.EMAIL_USE_TLS  
        )as connection:  
           subject = "Welcome to Testing"  
           email_from = settings.EMAIL_HOST_USER  
           recipient_list = [email, ]  
           message = "This email is to test the effectiveness of the platform just built, Now please proceed to something else. God bless"  
           EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()
    person = People.objects.create(name=name,email=email)
    person.save()
    return render(request, 'success.html', {'name':{'name':name}}) 
   