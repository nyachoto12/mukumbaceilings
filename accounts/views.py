from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .forms import CommentForm, SubscribeForm
from django.conf import settings

# Create your views here.
def home(request):
    subscribe=SubscribeForm
    if request.method=='GET':
        form=subscribe()
    else:
        form=subscribe(request.POST)
        if form.is_valid():
            
            contact_email = form.cleaned_data['contact_email']
            

            try:
                send_mail( '','','',contact_email, ['ngoninyachoto@gmail.com'])
                messages.info(request,'You have successfully subscribed to my newsletter')
   
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect ('/')

    return render(request,'accounts/home.html', {
        'form': CommentForm
     })
def login(request):
    if request.method=='POST':
             #saverecord=Users
             username=request.POST.get('username')
             password=request.POST.get('password')
             user=auth.authenticate(request,username=username,password=password)

             if user is not None:
                 auth.login(request,user)
                 messages.info(request,'Successfully Logged in')
                 return redirect('/')
             else:
                #messages.info(request,'Invalid credentials')
                return redirect("home")
    else:
         return render (request,'firstapp/login.html')
                   

   
def Contact(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('address') and request.POST.get('gender') and request.POST.get('subject') and request.POST.get('message'):

            saverecord=Users()
            saverecord.name=request.POST.get('name')
            saverecord.phone=request.POST.get('phone')
            saverecord.email=request.POST.get('email')
            saverecord.address=request.POST.get('address')
            saverecord.gender=request.POST.get('gender')
            saverecord.subject=request.POST.get('subject')
            saverecord.message=request.POST.get('message')
            saverecord.save()
            messages.success(request,'New User Added Successful')
            return redirect("/")

    else:
        return render (request,'accounts/contact.html')


def Services(request):
    return render (request,'accounts/services.html')

def Gallery(request):
    Contact_Form=CommentForm
    if request.method=='GET':
        form=Contact_Form()
    else:
        form=Contact_Form(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']

            try:
                send_mail(contact_name, contact_email, contact_message, ['ngoninyachoto@gmail.com'])
                messages.info(request,'Invalid credentials')
                
                
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect ('/')

    return render(request,'accounts/gallery.html', {'form': CommentForm })
    