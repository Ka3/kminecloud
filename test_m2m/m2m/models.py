from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Publication(models.Model):
    title = models.CharField(max_length=30)
    def __str__(self):              # __unicode__ on Python 2
        return self.title
    class Meta:
        ordering = ('title',)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)
    def __str__(self):              # __unicode__ on Python 2
        return self.headline
    class Meta:
        ordering = ('headline',)
