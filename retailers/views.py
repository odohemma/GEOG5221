from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Retailer
from .forms import RegistrationForm

# Create your views here.
class RetailersMapView(TemplateView):
    """Retailers map view."""

    template_name = "map.html"


class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url


class ProfileView(UpdateView):
    #The UpdateView is used for constructing simple forms. forms.ModelForm is used for the creation of sophisticated forms.
    model = Retailer
    fields = ['pms_rate', 'pms_stock', 'ago_rate', 'ago_stock', 'dpk_rate', 'dpk_stock', 
    'lpg_rate', 'lpg_stock', 'auto_shop', 'supermart', 'car_wash', 'name', 'phone', 'latitude',
    'longitude', 'picture']
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('home')

    def get_object(self):
        return self.request.user


class UserDelete(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('home')
    template_name = 'registration/user_confirm_delete.html'
