from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
#from  mukumba.models import Users
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail


@login_required
def home(request):
    return render (request,"home.html", {})