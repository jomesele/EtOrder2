from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager
# Create your models here.

class Customer(models.Model):
    customer=models.OneToOneField(User,on_delete=models.CASCADE)
    idno=models.IntegerField(blank=False)
    customer_type=models.CharField(max_length=256,blank=False)
    phone=models.IntegerField(default=0)
    ip_location = gis_models.PointField(null=True, blank=True, dim=3)
    
    is_customer=models.BooleanField(default=True)

    def __str__(self):
        return self.customer.username

class Staff(models.Model):
    staff=models.OneToOneField(User,on_delete=models.CASCADE)
    Staff_subject=models.CharField(max_length=256,blank=False)
    phone=models.IntegerField(default=0)
    is_customer=models.BooleanField(default=False)

    def __str__(self):
        return self.staff.username





