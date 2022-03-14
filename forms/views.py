from email import message
from tokenize import Name
from django.shortcuts import redirect, render,HttpResponse
from datetime import datetime
from forms.models import Contact, Destination ,Booking
from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("login succesfull")
            return redirect('booking')
        else:
            # message.info(request,"inavalid credential")
            return render(request,'login.html')
            
    else:
        return render(request,'login.html')
def registeruser(request):
    if request.method == 'POST':
        username=request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        if User.objects.filter(username=username).exists():
            # message.info(request,"username taken")
            print("username taken")
            return render(request,'register.html')
        elif User.objects.filter(email=email).exists():
            print("email taken")
            # message.info(request,"email taken")
            return render(request,'register.html')
        else:
            user = User.objects.create_user(  username=username,  password=password , email=email   )
            user.save()
            
        
            return redirect('login')
        
    else:
        return render(request,'register.html')


def booking(request):
    if request.user.is_anonymous:
        return redirect('login')
    if request.method == "POST":
        Name = request.POST.get('Name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        booking_date = request.POST.get('booking_date')
        booking_place = request.POST.get('booking_place')
        adult = request.POST.get('adult')
        children = request.POST.get('children')
        booking = Booking(Name=Name , email=email ,contact=contact , booking_date=booking_date , booking_place=booking_place , adult=adult , children=children )
        booking.save()
        
    
    return render(request,'booking.html')

def contact(request):
    if request.method =="POST":
        Name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        contact = Contact(Name=Name, email=email, desc=desc, phone=phone,date=datetime.today())
        contact.save()
        
    return render(request,'contact.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def bookings(request):
    allbookings=Booking.objects.filter(Name=request.user)
    context={'books':allbookings}
    return render(request,'bookings.html',context)