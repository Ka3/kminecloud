from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

Colour_choices = (('blue','blue'),
                  ('orange','orange'),
                  ('red','red'),
                  ('light','light'),
                  ('purple','purple'),
                  ('aqua','aqua'),
                  ('brown','brown'),
                  ('dark-blue','dark-blue'),
                  ('light-green','light-green'),
                  ('dark-red','dark-red'),
                  ('teal','teal')
                  )

class User_Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    Theme_colour = models.CharField(max_length=20,choices=Colour_choices,default='blue')
    def __str__(self):  
          return "%s's profile" % self.user  
      
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = User_Profile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 