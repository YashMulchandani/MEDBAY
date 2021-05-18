from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.core.paginator import Paginator
import datetime
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
import json
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
    # Pass quantity or update quantity
    return render(request, 'shop_single.html', {'data':data,'products':products, 'quantity': 1})

def cart(request):
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

# def update_Item(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#
#     print('action:', action)
#     print('productId:', productId)
#
#     customer = request.user.customer_name
#     product = ProductModel.objects.get(product_id=productId)
#     order, created = OrderModel.objects.get_or_create(
#         customer=customer, complete=False)
#
#     orderItem, created = OrderItem.objects.get_or_create(
#         order=order, product=product)
#
#     if action == 'add' or action == 'remove':
#         if action == 'add':
#             orderItem.quantity = (orderItem.quantity + 1)
#         elif action == 'remove':
#             orderItem.quantity = (orderItem.quantity - 1)
#
#         orderItem.save()
#
#     if orderItem.quantity <= 0:
#         orderItem.delete()
#     return JsonResponse('Item added to cart', safe=False)


def addItem(request, id, quantity):
    productId = id


    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product, quantity=quantity)
    
    # if action == 'add':
    #     orderItem.quantity = (orderItem.quantity + 1)
    # elif action == 'remove':
    #     orderItem.quantity = (orderItem.quantity - 1)
    # orderItem.save()

    if orderItem.quantity <=0:
       orderItem.delete()
    items = order.orderitem_set.all()
    print(order)

    return redirect('/cart')


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['from']['total'])
        order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
        order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],

        )
    else:
        print('user is not logged in..')
        return Response('payment-complete!', safe=False)
