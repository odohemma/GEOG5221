from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from bootstrap_datepicker_plus import DatePickerInput

from .models import Retailer


class RegistrationForm(forms.ModelForm):
    """ A class to allow new retailers to sign up."""

    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta:
        model = Retailer
        fields = ('username', 'name', 'address', 'local_government', 'state', 'latitude', 
        'longitude', 'email', 'phone', 'date_business_started', 'picture', 'password'
    )
        widgets = {
        'date_business_started': DatePickerInput()
    }

    def save(self, commit=True):
        # Hash and save the provided password.
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user



class RetailerCreationForm(forms.ModelForm):
    """A class to enable the superuser to create new accounts on the admin page."""

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = Retailer
        fields = ('username', 'email', 'name', 'phone', 'date_business_started', 'picture', 'is_staff', 'is_superuser')

    def clean_password2(self):
        # Confirm the two passwords submitted is a match.
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        # Hash the submitted provided and save it.
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class RetailerChangeForm(forms.ModelForm):
    """A class to enable the superuser to edit accounts of retailers on the admin page."""

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Retailer
        fields = ('username', 'email', 'name', 'phone', 'date_business_started', 'picture', 'password', 'is_active', 'is_superuser')

    def clean_password(self):
        # Notwithstanding whatever the user submits, return the initial value.
        return self.initial["password"]
