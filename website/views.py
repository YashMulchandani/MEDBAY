from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.core.paginator import Paginator
import datetime
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
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
    category = Category.objects.all()
    manufacture = Manufacturer.objects.all()

    return render(request, 'shop.html', {'products':products,'categories':category,'manufacturer':manufacture})

def filter_product(request, slug):
    products = Product.objects.filter(slug=slug)
    category = Category.objects.all()
    return render(request, 'category.html', {'products':products,'categories':category})

def manufacturer_product(request, slug):
    products = Product.objects.filter(manufacturer_slug=slug)
    manufacture = Manufacturer.objects.all()
    return render(request, 'manufacturer.html', {'products':products,'manufacturer':manufacture})

def shop_single(request, id,slug):
    data = Product.objects.get(id=id)
    products = Product.objects.filter(slug=slug).exclude(id=id)

    return render(request, 'shop_single.html', {'data':data,'products':products})


def cart(request):
#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#     else:
#         items = []
#         order = {'get_cart_total':0 ,'get_cart_items':0, 'shipping': False}
#         cartItems = order['get_cart_items']
#
     return render(request, 'cart.html', {})#'items':items, 'order':order})

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0 ,'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']

    return render(request, 'checkout.html', {'items':items, 'order':order})

def thankyou(request):
    return render(request, 'thankyou.html', {})


@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)

    if request.user.is_authenticated:
         customer = request.user.customer
         order, created = Order.objects.get_or_create(customer=customer, complete=False)
         items = order.orderitem_set.all()
         cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0 ,'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']

    return render(request, 'cart.html', {'items':items, 'order':order})

@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("shop.html")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("shop.html")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart.html')
