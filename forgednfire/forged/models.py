from django.db import models

# Create your models here.

class Forged(models.Model):

    name = models.CharField(max_length=100)
    length = models.IntegerField()
    blade = models.CharField(max_length=100)
    steelgrade = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True) 

    def get_blade_type(self):
       return self.name +"'s are in the " + self.blade + " family"

    def __repr__(self):
        return self.name + "is added"   

