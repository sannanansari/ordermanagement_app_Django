from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import upload,addcart
from .forms import *
from copy import deepcopy

def Home(request):
    return render(request,'Loginpage.html')

def Login(request):
    if request.method == 'POST':
  
        # AuthenticationForm_can_also_be_used__
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        print(email,password)
        user = authenticate(email=email,username=username, password=password)
        print(type(user))
        if user is not None:
            if str(user) == 'user':
                return redirect('userhomepage.html')
            elif str(user) == 'admin':
                return redirect('adminhomepage.html')
        else:
            return render(request,'Loginpage.html')
    form = AuthenticationForm()
    return render(request, 'Loginpage.html', {'form':form, 'title':'log in'})
# Create your views here.



def add_cart(request):
    raw = addcart.objects.all()
    upload1 = addcart()
    if request.method == 'POST':
        form = Uploadform(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return render(request, 'adminhomepage.html', {'raw': raw})

    return render(request, 'addcart.html',{'raw':raw})

def order(request):
    raw = addcart.objects.all()
    upload1 = addcart()
    if request.method == 'POST':
        form = Uploadform(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return render(request, 'adminhomepage.html', {'raw': raw})

    return render(request, 'order.html',{'raw':raw})


def upload_fetch(request):
    raw = upload.objects.all()
    upload2 = addcart()
    if request.method == 'POST':
        id_del = request.POST['id_order']
        form1 = Uploadform()
        try:
            instance = upload.objects.get(id1=id_del)
            upload2.id2 = instance.id1
            upload2.name2 = instance.name
            upload2.images2 = instance.images
            upload2.price2 = instance.price
            upload2.count2 = instance.count
            print(upload2)
            upload2.save()
            if instance.count>0:
                instance.count -= 1
                instance.save()
        except upload.DoesNotExist:
            user = None
            
        form = Uploadform()
    return render(request, 'userhomepage.html', {'raw': raw})


def add_product(request):
    raw = upload.objects.all()
    upload1 = upload()
    if request.method == 'POST':
        form = Uploadform(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return render(request, 'adminhomepage.html', {'raw': raw})
    else:
        temp = request.GET.get('id_del')
        if temp != 'None':
            id_del= temp
            try:
                instance = upload.objects.get(id=id_del)
                instance.delete()
            except upload.DoesNotExist:
                user = None
            
        form = Uploadform()
    return render(request, 'addproduct.html', {'form' : form})


def admin(request):
    raw = upload.objects.all()
    upload1 = upload()
    return render(request, 'adminhomepage.html', {'raw' : raw})