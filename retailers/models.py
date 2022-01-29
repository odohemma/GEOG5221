from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.validators import DecimalValidator, MaxValueValidator, MinValueValidator

# Create your models here.
""" class Product(models.Model):
    pms_rate = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Fuel: ₦/litre')
    pms_stock = models.BooleanField(default=False)
    ago_rate = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Diesel: ₦/litre')
    ago_stock = models.BooleanField(default=False)
    dpk_rate = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Kerosene: ₦/litre')
    dpk_stock = models.BooleanField(default=False)
    lpg_rate = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Cooking Gas: ₦/kg')
    lpg_stock = models.BooleanField(default=False)
    def __str__(self):
        return (
            f"PMS rate: {self.pms_rate} per litre \n"
            f"AGO rate: {self.ago_rate} per litre \n"
            f"DPK rate: {self.dpk_rate} per litre \n"
            f"LPG rate: {self.lpg_rate} per kg"
        ) """


class RetailerManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, name, phone, password, **extra_fields):
        values = [username, name, phone]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value is required'.format(field_name))

        user = self.model(
            username=username,
            name=name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, name, phone, password, **extra_fields)

    def create_superuser(self, username, name, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, name, phone, password, **extra_fields)


class Retailer(AbstractBaseUser, PermissionsMixin):    
    username = models.CharField(unique=True, max_length=150)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    local_government = models.CharField(max_length=150, verbose_name="Local Government")
    state = models.CharField(max_length=150)    
    latitude = models.DecimalField(blank=True, null=True, validators=[MinValueValidator(-90.0), MaxValueValidator(90.0), DecimalValidator (max_digits=10, decimal_places=6)], max_digits=10, decimal_places=6, help_text="Kindly input the WGS84 latitude and, restrict the values to a maximum of six decimal places.<br/> Unless you intend to change your location, you can skip this section in the profile page.")
    longitude = models.DecimalField(blank=True, null=True, validators=[MinValueValidator(-180.0), MaxValueValidator(180.0), DecimalValidator (max_digits=10, decimal_places=6)], max_digits=10, decimal_places=6, help_text="Kindly input the WGS84 longitude and, restrict the values to a maximum of six decimal places.<br/> Unless you intend to change your location, you can skip this section in the profile page.")

    email = models.EmailField(unique=True, null=True, blank=True)    
    phone = models.CharField(max_length=50)
    picture = models.ImageField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_business_started = models.DateField(blank=True, null=True)
    date_profile_updated = models.DateTimeField(default=timezone.now)

    # GeoDjango-specific: a geometry field (PointField)
    coordinates = models.PointField(blank=True, null=True, spatial_index=True)

    #Products
    pms_rate = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Petrol: ₦/litre', default=0)
    pms_stock = models.BooleanField(verbose_name='Petrol in stock?', default=False)
    ago_rate = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Diesel: ₦/litre', default=0)
    ago_stock = models.BooleanField(verbose_name='Diesel in stock?', default=False)
    dpk_rate = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Kerosene: ₦/litre', default=0)
    dpk_stock = models.BooleanField(verbose_name='Kerosene in stock?', default=False)
    lpg_rate = models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Cooking Gas: ₦/kg', default=0)
    lpg_stock = models.BooleanField(verbose_name='Cooking Gas in stock?', default=False)
    
    #Extras
    auto_shop = models.BooleanField(verbose_name='Auto Shop', default=False)
    supermart = models.BooleanField(default=False)

    objects = RetailerManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'phone']


    def save(self, *args, **kwargs):
        self.latitude = self.latitude
        self.longitude = self.longitude

        # Point is obtained from latitude/longitude
        # The srid for WGS84 Geographic Coordinate System is 4326
        if self.longitude and self.latitude:
            self.coordinates = Point(
                float(self.longitude),
                float(self.latitude),
                srid=4326
            )
        else:
            self.coordinates = None
        super().save(*args, **kwargs)

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name.split()[0]
