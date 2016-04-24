from django.conf import settings
from django.db import models

# Create your models here.



class Auditable(models.Model):
    created_on = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_Created_By')

    modified_on = models.DateTimeField(auto_now = True)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_modified_by')

    class Meta:
        abstract = True
