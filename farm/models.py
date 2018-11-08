from django.db import models

class Article(models.Model):
    title = models.CharField(max_length =60)
    description = models.TextField(max_length =1000, null=True)
    image = models.ImageField(upload_to='index/', default=True)

class Location(models.Model):
    name = models.CharField(max_length=25)
    AREA_CHOICES = (
        ('Westlands', 'Westlands Constituency'),
        ('Dagoretti', 'Dagoretti Constituency'),
        ('Langata', 'Langata Constituency'),
        ('Kasarani', 'Kasarani Constituency'),
        ('Embakasi', 'Embakasi Constituency'),
        ('Starehe', 'Starehe Constituency'),
        ('Kamkunji', 'Kamkunji Constituency'),
    )
    area = models.CharField(max_length = 25, choices = AREA_CHOICES)

# class Contacts(models.Model):
    