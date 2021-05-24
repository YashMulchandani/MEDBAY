from django.urls import path
from . import views
# from website.views import CheckoutView
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.signup, name="register"),
    path('login/', views.login_User, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('search/', views.search, name="search"),
    path('your_profile/', views.your_profile, name="your_profile"),
    path('home/', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('shop/', views.shop, name="shop"),
    path('shop_single/<int:id>/<str:slug>/', views.shop_single, name="shop_single"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    # path('CheckoutView/', CheckoutView.as_view(), name="CheckoutView"),
    path('thankyou/', views.thankyou, name="thankyou"),
    path('add_item/<int:id>/<int:quantity>/', views.addItem, name="add_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('category/<str:slug>/', views.filter_product, name="category"),
    path('manufacturer/<str:slug>/', views.manufacturer_product, name="manufacturer"),
    #path('update_item', views.update_Item, name="update_item")
    # Create different method to update the items, (update the quantity)
    # Total will be automaticall calculated from property functions


    # path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    # path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    # path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    # path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    # path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    # path('cart/cart-detail/',views.cart_detail,name='cart_detail'),


]
