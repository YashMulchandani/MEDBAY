from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from website import models as website_models


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    First_name = forms.CharField(required=True)
    Last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username","First_name", "Last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.First_name = self.cleaned_data['First_name']
        user.Last_name = self.cleaned_data['Last_name']
        if commit:
            user.save()
            # Creating record in Customer table
            website_models.Customer.objects.get_or_create(
                user=user, fname=user.First_name, lname=user.Last_name, email=user.email
            )
        return user
