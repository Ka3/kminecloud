from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from uuid import uuid4
# Create your models here.

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    filename = str(uuid4().hex) + str(filename)
    return 'user_{0}/{1}'.format(instance.first_name, filename)

class Person(models.Model):
 	Gender_Choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T', 'TransGender'),
   			 )
	first_name = models.CharField("First Name",max_length=30)
	last_name = models.CharField(max_length=30)
	E_Mail = models.EmailField()
	Council = models.CharField(max_length=100)
        Date_of_Birth = models.DateField()
        Photo = models.ImageField(null=True,blank=True, upload_to=user_directory_path)
	Age = models.IntegerField()
	Gender = models.CharField(max_length=1, choices=Gender_Choices)
	Address_Line1 = models.CharField(max_length=100)
	Address_Line2 = models.CharField(max_length=100)
	Post_Code = models.CharField(max_length=100)
	City = models.CharField(max_length=100)
        created     = models.DateTimeField(editable=False)
        modified    = models.DateTimeField()       
        def __unicode__ (self):
                return self.first_name + ' ' + self.last_name
      
        def get_absolute_url(self):
                pass
        class Meta:
                ordering = ['-modified','-created']
                
        def save(self, *args, **kwargs):
            ''' On save, update timestamps '''
            if not self.id:
                self.created = timezone.now()
            self.modified = timezone.now()
            return super(Person, self).save(*args, **kwargs)
    


