from django.contrib import admin
from .models import *

class Customer_admin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email')

class Product_admin(admin.ModelAdmin):
    list_display = ('name', 'mg', 'category', 'manufacturer', 'price')

class Order_admin(admin.ModelAdmin):
    list_display = ('customer', 'complete')

class Order_item_admin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity')

class ShippingAddress_admin(admin.ModelAdmin):
    list_display = ('fname', 'address1', 'country', 'state', 'zipcode' )

class Category_admin(admin.ModelAdmin):
    list_display = ('title', 'slug')

class Manufacturer_admin(admin.ModelAdmin):
    list_display = ('title', 'slug')
admin.site.register(Customer, Customer_admin)
admin.site.register(Product, Product_admin)
admin.site.register(Order, Order_admin)
admin.site.register(OrderItem, Order_item_admin)
admin.site.register(ShippingAddress, ShippingAddress_admin)
admin.site.register(Category, Category_admin)
admin.site.register(Manufacturer, Manufacturer_admin)
