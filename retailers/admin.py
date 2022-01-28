from django.contrib import admin
from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Retailer
from .forms import UserCreationForm, UserChangeForm

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "pms_rate", "pms_stock", "ago_rate", "ago_stock", "dpk_rate", "dpk_stock", "lpg_rate", "lpg_stock", "auto_shop", "supermart")

class RetailerAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'username', 'email', 'name', 'phone', 'date_business_started', 
    'is_staff', 'is_superuser', 'latitude', 'longitude', 'coordinates', 'pms_rate', 'pms_stock', 
    'ago_rate', 'ago_stock', 'dpk_rate', 'dpk_stock', 'lpg_rate', 'lpg_stock', 'auto_shop', 'supermart')
    list_filter = ('is_superuser',)

    fieldsets = (
        (None, {'fields': ('username', 'email', 'is_staff', 'is_superuser', 'password')}),
        ('Retailer information', {'fields': ('name', 'phone', 'date_business_started', 'address', 'local_government', 'state', 'latitude', 'longitude', 'picture', 'pms_rate', 'pms_stock', 'ago_rate', 'ago_stock', 'dpk_rate', 'dpk_stock', 'lpg_rate', 'lpg_stock', 'auto_shop', 'supermart')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'is_staff', 'is_superuser', 'password1', 'password2')}),
        ('Retailer information', {'fields': ('name', 'phone', 'date_business_started', 'address', 'local_government', 'state', 'latitude', 'longitude', 'picture', 'pms_rate', 'pms_stock', 'ago_rate', 'ago_stock', 'dpk_rate', 'dpk_stock', 'lpg_rate', 'lpg_stock', 'auto_shop', 'supermart')}),
        ('Groups', {'fields': ('groups',)}),
        ('Permissions', {'fields': ('user_permissions',)}),
    )

    search_fields = ('username', 'email', 'name', 'phone')
    ordering = ('id',)
    filter_horizontal = ()

admin.site.register(Retailer, RetailerAdmin)