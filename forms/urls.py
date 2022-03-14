from django import views
from django.contrib import admin
from django.urls import path
from forms import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('contact',views.contact,name='contact'),
    path('register',views.registeruser,name='register'),
    path('booking',views.booking,name='booking'),
    path('logout',views.logout,name='logout'),
    path('bookings',views.bookings,name='bookings')
]