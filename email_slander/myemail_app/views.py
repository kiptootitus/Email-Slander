from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(
            username = username,
            email = email, 
            password = password
            )
        login (request, user)
        subject = 'Welcome to Email Slander'
        message = 'Thank you for signing up to Email Slander'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_email = send_mail(subject, message, email_from, recipient_list)
        return redirect('/dashboard/')