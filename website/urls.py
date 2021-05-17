from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('shop/', views.shop, name="shop"),
    path('shop_single/<int:id>/<str:slug>/', views.shop_single, name="shop_single"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('thankyou/', views.thankyou, name="thankyou"),
    #path('update_Item/', views.updateItem, name="update_Item"),
    #path('process_order/', views.processOrder, name="process_order"),
    path('category/<str:slug>/', views.filter_product, name="category"),
    path('manufacturer/<str:slug>/', views.manufacturer_product, name="manufacturer"),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),


]
