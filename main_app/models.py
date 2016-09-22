from __future__ import unicode_literals

from django.db import models

from django.utils import timezone


# Create your models here.

class Country(models.Model):
    Name = models.CharField(max_length=200)
    Basics = models.TextField()
    
    def __str__(self):
        return self.Name

class School(models.Model):
    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Location = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    Basics = models.TextField()
    Rating = models.DecimalField(max_digits=4, decimal_places=2)
    Website = models.CharField(max_length=100)
    Email = models.EmailField(max_length=200)
    #Photos = models.ImageField()

    def __str__(self):
        return self.Name

class Formation(models.Model):
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    Name = models.CharField(max_length=200)
    Description = models.TextField()
    Pre_basics = models.TextField()

    def __str__(self):
        return self.Name

class Post(models.Model):
    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




