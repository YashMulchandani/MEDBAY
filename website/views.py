from django.shortcuts import render
from django.core.mail import send_mail
from .models import *

def index(request):
    return render(request, 'index.html', {})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def contact(request):
    if request.method == "POST":
        c_fname = request.POST['c_fname']
        c_lname = request.POST['c_lname']
        c_email = request.POST['c_email']
        c_message = request.POST['c_message']

        # Send an E-mail
        send_mail(
            c_fname,# Subject
            c_message,# Message
            c_email,# from_email
            ['yash.mulchandani575@gmail.com'],# to_email
            )

        return render(request, 'contact.html', {'c_fname':c_fname})
    else:
        return render(request, 'contact.html', {})

def about(request):
    return render(request, 'about.html', {})


def shop(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products':products})


def shop_single(request):
    return render(request, 'shop_single.html', {})

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 ,'get_cart_items':0}

    return render(request, 'cart.html', {'items':items, 'order':order})

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0 ,'get_cart_items':0}

    return render(request, 'checkout.html', {'items':items, 'order':order})
