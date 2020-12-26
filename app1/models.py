from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Vehicle(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    reg_no = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    seats = models.IntegerField(null=True, blank=True)
    ac = models.BooleanField(default=True)
    multiplier = models.FloatField(null=True, blank=True)


class VehicleBookings(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    destination = models.CharField(max_length=100, blank=True, null=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    kilometers = models.IntegerField(null=True, blank=True)
    vehicle = models.ForeignKey(to=Vehicle, related_name='vehi', on_delete=models.CASCADE)


class Hotel(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    no_of_rooms = models.IntegerField(null=True, blank=True)
    cost_ac = models.FloatField(null=True, blank=True)
    cost_non_ac = models.FloatField(null=True, blank=True)
    cost_per_person = models.FloatField(null=True, blank=True)


class HotelBooking(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    room_no = models.IntegerField(null=True, blank=True)
    ac = models.BooleanField(default=True)
    cost = models.FloatField(null=True, blank=True)
    hotel = models.ForeignKey(to=Hotel, related_name='hotel', on_delete=models.CASCADE)


class UserExtend(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    ph_no = models.CharField(max_length=15, null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserExtend.objects.create(user=instance)
        instance.save()


class VehicleHistory(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    old_multiplier = models.FloatField(null=True, blank=True)
    new_multiplier = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField()


class HotelHistory(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    old_cost_ac = models.FloatField(null=True, blank=True)
    new_cost_ac = models.FloatField(null=True, blank=True)
    old_cost_non_ac = models.FloatField(null=True, blank=True)
    new_cost_non_ac = models.FloatField(null=True, blank=True)
    old_cost_per_person = models.FloatField(null=True, blank=True)
    new_cost_per_person = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField()