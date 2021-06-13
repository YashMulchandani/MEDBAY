from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# TABLE FOR CUSTOMER
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, null=True)
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)


    def __str__(self):
        return self.fname


# TABLE FOR CATEGORIES
class Category(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.title


# TABLE FOR Manufacturer
class Manufacturer(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural='Manufacturer'

    def __str__(self):
        return self.title


# Table for Product
class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    slug = models.SlugField(max_length=200, db_index=True ,null = True)
    name = models.CharField(max_length=200, null=True)
    detail = models.TextField(max_length=1000, null=True, blank=True)
    mg = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(null=True, blank=True)
    manufacturer_slug = models.SlugField(max_length=200, db_index=True ,null = True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)
    storage = models.FloatField(null=True, blank=True)
    uses = models.TextField(max_length=1000, null=True, blank=True)
    side_effect = models.TextField(max_length=1000, null=True, blank=True)
    benifits = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


# Table for ORDER
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    complete = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return str(self.id)


#function to get cart total
    @property
    def get_cart_total(self):
        orderitems = OrderItem.objects.filter(order_id=self.id)
        total = sum([item.get_total for item in orderitems])
        return total

# Function to get total cart items
    @property
    def get_cart_items(self):
        orderitems = OrderItem.objects.filter(order_id=self.id)
        total = sum([item.quantity for item in orderitems])
        return total

# Table for Order Item
class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


# Table for Shipping Address
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    #order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address1 = models.CharField(max_length=200, null=True)
    address2 = models.CharField(max_length=200, null=True)
    country = CountryField(multiple=False, null=True)
    state = models.CharField(max_length=200, null=True)

    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    save_info = models.BooleanField(default=False)
