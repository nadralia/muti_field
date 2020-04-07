from django.db import models
import uuid
from api.apps.accounts.models import Company, User
from api.apps.inquiry.models import Inquiry

# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=250, default='')
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'activities'


class Day(models.Model):
    daytype = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="day_user")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE,
                                   related_name="activity_day") 
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'days'


class Guide(models.Model):
    guide_name = models.CharField('guide_name', max_length=100)
    guide_phone = models.CharField(max_length=15, default='')
    class Meta:
        db_table = 'guides'


class Driver(models.Model):
    driver_name = models.CharField('driver_name', max_length=100)
    driver_phone = models.CharField(max_length=15, default='')

    class Meta:
        db_table = 'drivers'


class Vehicle(models.Model):
    vehicle_number = models.CharField('vehicle_number', max_length=16)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, 
                                        related_name="vehicle_driver")
    class Meta:
        db_table = 'vehicles'


class Itinerary(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name="itinerary_company")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="itinerary_user")
    inquiry = models.ForeignKey(Inquiry, on_delete=models.CASCADE,
                                   related_name="itinerary_inquiry")
    day = models.ForeignKey(Day, on_delete=models.CASCADE,
                                   related_name="itinerary_day") 
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, 
                                       related_name="itinerary_vehicle")
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, 
                                       related_name="itinerary_guide")                        
    itineraryname = models.CharField(max_length=250, default='')
    numberadults = models.IntegerField()
    numberchildren = models.IntegerField()
    itinerarystatus = models.IntegerField(default=0)
    monthyear = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'itineraries'
