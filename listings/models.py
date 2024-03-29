from django.db import models
from django.utils import timezone
from realtors.models import Realtor
from .choices import neighborhood_choice
class Listing(models.Model):
    PROPERTY_TYPES = (
        ('SFR', 'House'),
        ('CNDO', 'Condo'),
        ('TWNH', 'Townhouse'),
        ('MFR', 'Mulit-Family'),
        ('LND', 'Land'),
        ('OTHR', 'Other'),
    )
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=200, choices=neighborhood_choice.items())
    address = models.CharField(max_length=200)
    city = models.CharField(default="Chicago", max_length=100)
    state = models.CharField(default='IL', max_length=100)
    zipcode = models.CharField(max_length=20)
    build_type = models.CharField(max_length=4, choices=PROPERTY_TYPES)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.title