from sys import path

from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact, Add
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def fruit(request):
    if request.method == 'POST':
        name_product = request.POST.get('product')
        price = request.POST.get('price')
        num = request.user.id
        cart = Add(num=num, prod_name=name_product, price=price)
        cart.save()
    return render(request, 'fruit.html')


def vegetables(request):
    if request.method == 'POST':
        name_product = request.POST.get('product')
        price = request.POST.get('price')
        num = request.user.id
        cart = Add(num=num, prod_name=name_product, price=price)
        cart.save()
    return render(request, 'veg.html')


def daily(request):
    if request.method == 'POST':
        name_product = request.POST.get('product')
        price = request.POST.get('price')
        num = request.user.id
        cart = Add(num=num, prod_name=name_product, price=price)
        cart.save()
    return render(request, 'groc.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phn')
        desc = request.POST.get('desc')
        con = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        con.save()
        messages.success(request, 'Your message has been sent successfully')
    return render(request, 'contact.html')


def log(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully Logged In!')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('home')
    return render(request, 'registration/login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email1 = request.POST.get('email')
        password1 = request.POST.get('pass')
        user = User.objects.create_user(username=name, password=password1, email=email1)
        user.save()
    return render(request, 'registration/signup.html')


def cart(request):
    x = request.user.id
    count = Add.objects.filter(num=x).count()
    item = Add.objects.filter(num=x)
    c = 0
    for i in item:
        c = c + i.price
    t = 0
    if c != 0:
        t = c + 20
    context = {
        'count': count,
        'items': item,
        'subtotal': c,
        'total': t
    }
    if request.method == 'POST':
        messages.success(request, 'ORDERED!, Your order has been successfully placed')
    return render(request, 'cart.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')
