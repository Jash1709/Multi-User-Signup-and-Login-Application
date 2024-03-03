from django.shortcuts import render,redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import *
import re
# Create your views here.
def login(req):
    if req.method == "POST":
        username = req.POST['username']
        password = req.POST['password']
        User = user.objects.filter(username=username, password=password).first()

        if User is not None:
            if User.usertype == 'doctor':

                return render(req,"doctordashboard.html",{'user':User})
            else:
                return render(req,"clientdashboard.html",{'user':User})
        else:
            return HttpResponse("error")
    else:
        return render(req,"login.html")

def signup(req):
    if req.method == 'POST':
        utype = req.POST['uservalue']
        fname = req.POST['firstname']
        lname = req.POST['lastname']
        email = req.POST['email']
        username = req.POST['username']
        password = req.POST['pass']
        cpass = req.POST['cpass']
        line1 = req.POST['line1']
        city = req.POST['city']
        state = req.POST['state']
        pincode = req.POST['pincode']
        profile_photo = req.FILES.get('pphoto')

        if len(password) < 8 or not any(c.isdigit() for c in password) or not any(c.isalpha() for c in password):
            return HttpResponse("Password must be at least 8 characters long and contain both alphabetic and numeric characters.")

        

        if password == cpass:
            user_instance = user.objects.create(
                usertype=utype,
                firstname=fname,
                lastname=lname,
                email=email,
                username=username,
                password=password,
                cpassword=cpass,
                line1=line1,
                city=city,
                state=state,
                pincode=pincode,
                pphoto=profile_photo,
            )            
            user_instance.save()
            return redirect("login")
        else:
            return HttpResponse("password does not match")
    else:
        return render(req,"signup.html")
        
def dashboard(req):
    if req.user.is_authenticated and req.user.usertype == 'doctor':
        return render(req, "doctordashboard.html", {'user': req.user})
    else:
        return redirect('login')

def client_dashboard(req):
    if req.user.is_authenticated and req.user.usertype == 'client':
        return render(req, "clientdashboard.html", {'user': req.user})
    else:
        return HttpResponse("Unauthorized", status=401)
def user_logout(req):
    logout(req)
    return redirect('login')