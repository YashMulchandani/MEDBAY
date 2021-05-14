from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('home.html', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('shop.html', views.shop, name="shop"),
    path('shop_single.html/', views.shop_single, name="shop_single"),
	path('cart.html', views.cart, name="cart"),
	path('checkout.html', views.checkout, name="checkout"),
    path('update_Item', views.update_Item, name="update_Item"),
    path('process_order', views.processOrder, name="process_order"),
]
