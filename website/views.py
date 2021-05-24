from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.http import JsonResponse
from django.core.paginator import Paginator
import datetime
from django.contrib.auth.decorators import login_required
#from cart.cart import Cart
from .forms import *
import json
from .models import *
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .decorators import unauthenticated_user
from django.views import View


#@unauthenticated_user
def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            messages.success(request, f' welcome {username} !!')
            return redirect("home")
    else:
        form = NewUserForm()
    return render(request, 'register.html', {'form': form})

@unauthenticated_user
def login_User(request):

    if request.method == 'POST':

        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'login.html', {'login_form':form})


def logout_user(request):
    logout(request)
    messages.success(request, 'you are logged out')
    return redirect('home')

def index(request):
    return render(request, 'index.html', {})

def search(request):
    q = request.POST['q']
    products = Product.objects.filter(name__icontains=q).order_by('id')
    products = Product.objects.filter(mg__icontains=q).order_by('id')
    print(products)
    return render(request, 'search.html', {'q':q, 'products': products})

def your_profile(request):
    return render(request, 'your_profile.html', {})

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
    print(request)
    data = Product.objects.get(id=id)
    products = Product.objects.filter(slug=slug).exclude(id=id)
    # Pass quantity or update quantity
    return render(request, 'shop_single.html', {'data':data,'products':products, 'quantity':1})

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
    # productId = id
    # customer = request.user.customer
    # product = Product.objects.get(id=productId)
    # order_item = OrderItem.objects.create(product=product)
    # order_qs = Order.objects.filter(customer=request.user.customer, complete=False)
    # if order_qs.exists():
    #     order = order_qs[0]
    #     if order.product.filter(product__id ==product.id).exists():
    #         order_item.quantity += 1
    #         order_item.save()
    # else:
    #     order = Order.objects.create(customer=request.user.customer)
    #     order.product.add(order_item)
    #     return redirect("cart", kwargs={'id':id})
    #






    productId = id
    print(quantity)

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

def checkout(request):
    form = AddressForm()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0 ,'get_cart_items':0, 'shipping': False}
        cartItems = order['get_cart_items']


    if request.GET:
        order = Order.objects.get(user=self.request.user, ordered=False)
        # address = Address.objects.get(user=self.request.user, default=True)
        coupon_form = CouponForm()
        form = AddressForm()
        context = {
            'form': form,
            'order': order,
            }

    elif request.POST:
        order = Order.objects.get(user=self.request.user, ordered=False)
        form = AddressForm(self.request.POST or None)
        if form.is_valid():

            address1 = form.cleaned_data.get('address1')
            address2 = form.cleaned_data.get('address2')
            country = form.cleaned_data.get('country')
            state = form.cleaned_data.get('state')
            zipcode = form.cleaned_data.get('zipcode')
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            save_info = form.cleaned_data.get('save_info')
            use_default = form.cleaned_data.get('use_default')

            address = ShippingAddress(
                user=self.request.user,
                address1=address1,
                address2=address2,
                country=country,
                zipcode=zipcode,
            )
            address.save()
            if save_info:
                address.default = True
                address.save()

            order.address = address
            order.save()

            if use_default:
                address = ShippingAddress.objects.get(user=self.request.user, default=True)
                order.address = address
                order.save()

    # if request.POST:
    #     form = Billing_detail(request.POST or None)
    #     if form.is_valid():
    #         customer = Customer.objects.get(user=user)
    #         print(customer)
    #         ShippingAddress.objects.create(customer=customer, state=user.userstate, country=user.country, address1=user.address1,
    #         address2=user.address2, fname=user.fname, lname=user.lname, zipcode=user.zipcode, save_info=user.save_info, use_default=user.use_default)
    #         #print(form.cleaned_data)
    #     else:
    #         print("Form Invalid")
    # elif request.GET:
    #     form = Billing_detail()
    # print(form)
    return render(request, 'checkout.html', {'items':items, 'order':order,'form':form})


# class CheckoutView(View):
#
#     # def get(self, *args, **kwargs):
#         form = Billing_detail()
#         context = {
#         "form":form
#         }
#         return render(self.request, 'checkout.html', context)
#
#     # def post(self, *args, **kwargs):
#         form = Billing_detail(self.request.POST or None)
#         if form.is_valid():
#             print(form.cleaned_data)
#         else:
#             print("Form Invalid")
