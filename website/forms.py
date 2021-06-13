from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from website import models as website_models
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget



class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    First_name = forms.CharField(required=True)
    Last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username","First_name", "Last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.First_name = self.cleaned_data['First_name']
        user.Last_name = self.cleaned_data['Last_name']
        if commit:
            user.save()
            # Creating record in Customer table
            website_models.Customer.objects.get_or_create(
                user=user, username = user.username, fname=user.First_name, lname=user.Last_name, email=user.email
            )
        return user

class AddressForm(forms.Form):
    address1 = forms.CharField(required=True)
    address2 = forms.CharField(required=True)
    country = CountryField().formfield(widget=CountrySelectWidget(attrs={"class":"form-control"}))
    state = forms.CharField(required=True)
    fname = forms.CharField(required=True)
    lname = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)
    save_info = forms.BooleanField(required=False)
    #use_default = forms.BooleanField(required=False)


    class Meta:
        model = website_models.ShippingAddress
        fields = ('address1','address2','country',"state", "fname", "lname", "zipcode")

    def save(self, commit=True):
        user = super(Billing_detail, self).save(commit=False)
        user.address1 = self.cleaned_data['address1']
        user.address2 = self.cleaned_data['address2']
        user.country = self.cleaned_data['country']
        user.state = self.cleaned_data['state']
        user.fname = self.cleaned_data['fname']
        user.lname = self.cleaned_data['lname']
        user.zipcode = self.cleaned_data['zipcode']
        user.save_info = self.cleaned_data['save_info']
        #user.use_default = self.cleaned_data['use_default']

        if commit:
            user.save()
            # Creating record in Customer table
            website_models.Customer.objects.get(
                customer=customer)
        return user
