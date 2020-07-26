from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from localflavor.br.forms import BRPostalCodeField

# Create your models here.
from django.http import request


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture_url = models.ImageField(upload_to='profile_picture/', default='static/assets/images/default_user.png', blank=True, null=True)
    phone = models.CharField(max_length=120, blank=False, null=True, default=None)
    cpf = models.CharField(max_length=120, blank=False, null=True, unique=True, default=None)
    birth_date = models.DateField(blank=False, null=True, default=None)
    wallet = models.DecimalField(default=0, max_digits=6, decimal_places=2, blank=False, null=False)
    psn_gametag = models.CharField(max_length=120, blank=False, null=True, default=None)
    xbox_gametag = models.CharField(max_length=120, blank=False, null=True, default=None)
    bank_name = models.CharField(max_length=120, blank=False, null=True, default=None)
    bank_account = models.CharField(max_length=120, blank=False, null=True, unique=True, default=None)
    bank_agency = models.CharField(max_length=120, blank=False, null=True, unique=True, default=None)
    bank_digit = models.CharField(max_length=120, blank=False, null=True, unique=True, default=None)
    user_status = models.CharField(max_length=120, default='available', blank=False, null=False)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

