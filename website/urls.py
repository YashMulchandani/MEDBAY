from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('shop/', views.shop, name="shop"),
    path('shop_single/<str:slug>/<int:id>/', views.shop_single, name="shop_single"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('update_Item/', views.updateItem, name="update_Item"),
    path('process_order/', views.processOrder, name="process_order"),
]
