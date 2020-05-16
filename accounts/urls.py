from django.urls import path,reverse
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns=[
    path('',views.home, name='home'),
   # path('register',views.register, name='register'),
    path('login',views.login, name='login'),
    path('gallery',views.Gallery, name='gallery'),
    path('contact',views.Contact, name='contact'),
    path('services',views.Services, name='services')
]