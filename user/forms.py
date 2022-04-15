from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from user.models import User


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "name",
            "date",
            "email",
            "income",
            "ipaddress"
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "date": forms.DateInput(attrs={"class": "form-control "}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "income": forms.NumberInput(attrs={"class": "form-control"}),
            "ipaddress": forms.TextInput(attrs={"class": "form-control"})

        }
