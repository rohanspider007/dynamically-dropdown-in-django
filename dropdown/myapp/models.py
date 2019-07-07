from django.db import models

# Create your models here.

class Country(models.Model):
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.country

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.state