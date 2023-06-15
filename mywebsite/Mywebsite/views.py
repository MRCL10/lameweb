from django import template
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'base/home.html')
def index(request):
    return render(request, 'base/home.html')

def send_email(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')


    subject = 'WEBSITE CONTACT FORM SUBMISSION'
    body = f'name: {name}\nEmail: {email}\nSubject: {subject}\nMessage:{message}'
    sender = name
    sender_email = email
    recipient_list = ['mrclcode100@gmail.com']

    send_mail(subject, body, email, recipient_list, sender_email)

    return HttpResponse('Email sent successfully')


