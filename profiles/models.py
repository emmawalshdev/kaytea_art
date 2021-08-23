from django.db import models
from django.contrib.auth.models import User
#import signals for use after save
from django.db.models.signals import post_save
# import reciever to get signals
from django.dispatch import receiver

from django_countries.fields import CountryField


# Create your models here.
class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery info and order history
    """
    # specify one user profile to one user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_first_name = models.CharField(max_length=50, null=True, blank=True)
    default_last_name = models.CharField(max_length=50, null=True, blank=True)
    default_email = models.CharField(max_length=254, null=True, blank=True)
    default_mobile_number = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_address_line1 = models.CharField(max_length=80, null=True, blank=True)
    default_address_line2 = models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label="Country *", null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)

    # string method to return user name
    def __str__(self):
        return self.user.username


# update or create profile each time object is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()