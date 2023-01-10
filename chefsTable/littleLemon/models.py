from django.db import models
from django.db import models

# Create your models here.


class Menu(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name + ' ' + self.cuisine
    
class Person(models.Model): 
    person_name = models.CharField(max_length=20) 
    person_age = models.IntegerField() 
    email = models.EmailField() 
    phone = models.CharField(max_length=20) 