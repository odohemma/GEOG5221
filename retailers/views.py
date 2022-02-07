from django.views.generic.base import TemplateView
from django.contrib.auth import get_user_model

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Retailer
from .forms import RegistrationForm

# Create your views here.
class RetailersMapView(TemplateView):
    """Retailers map view."""

    template_name = "map.html"


class RegistrationView(CreateView):
    """This class serves the webpage needed for a retailer to get registered on the app."""

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
    """A class to serve a webpage that allow a retailer to update the outlet's profile."""

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
    """A class to enable a retailer delete the outlet's account from the database."""
    
    model = get_user_model()
    success_url = reverse_lazy('home')
    template_name = 'registration/user_confirm_delete.html'
