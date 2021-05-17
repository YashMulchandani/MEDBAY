from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('shop/', views.shop, name="shop"),
    path('shop_single/<int:id>/', views.shop_single, name="shop_single"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('add_item/<int:id>/<int:quantity>/', views.addItem, name="add_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
# Create different method to update the items, (update the quantity)
# Total will be automaticall calculated from property functions