from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings

urlpatterns = [
    #path("favicon.ico", RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),  name= 'favicon'),
#LOADER
    path('', views.index, name="index"),

#REGISTRATION
    path('register/', views.signup, name="register"),
    path('login/', views.login_User, name="login"),
    path('logout/', views.logout_user, name="logout"),

#NAVIGATION BAR
    path('search/', views.search, name="search"),
    path('home/', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('shop/', views.shop, name="shop"),
    path('shop_single/<int:id>/<str:slug>/', views.shop_single, name="shop_single"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('thankyou/', views.thankyou, name="thankyou"),
    path('add_item/<int:id>/<int:quantity>/', views.addItem, name="add_item"),
    # path('process_order/', views.processOrder, name="process_order"),
    path('category/<str:slug>/', views.filter_product, name="category"),
    path('manufacturer/<str:slug>/', views.manufacturer_product, name="manufacturer"),
    path('use_default_address/<int:id>', views.use_default_address,name='use_default_address'),

# PASSWORD
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), name='password_reset_complete'),
    path('update_item', views.update_Item, name="update_item"),
]
