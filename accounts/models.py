from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from . import retrieve
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='Profile')
	followers=models.IntegerField(default=0)
	last_updated=models.DateTimeField(default=datetime.now())

class Repository(models.Model):
	profile=models.ForeignKey(Profile,on_delete=models.CASCADE,)
	name=models.CharField(max_length=150,default='')
	stars=models.IntegerField(default=0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
		instance.Profile.save()
		retrieve.Store(instance)