from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.fname


class Category(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural='2. Categories'

    def __str__(self):
        return self.title

class Manufacturer(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    slug = models.SlugField(max_length=200, db_index=True ,null = True)
    name = models.CharField(max_length=200, null=True)
    detail = models.TextField(max_length=1000, null=True, blank=True)
    mg = models.FloatField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    images = models.ImageField(null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)
    storage = models.FloatField(null=True, blank=True)
    uses = models.TextField(max_length=1000, null=True, blank=True)
    side_effect = models.TextField(max_length=1000, null=True, blank=True)
    benifits = models.TextField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_cat_list(self):
        k = self.category # for now ignore this instance method

        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug_cat)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]

    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

        @property
        def shipping(self):
            shipping = False
            orderitems = self.orderitem_set.all()
            for i in orderitems:
                if i.product.digital == False:
                   shipping = True
            return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    fname = models.CharField(max_length=200, null=True)
    lname = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
