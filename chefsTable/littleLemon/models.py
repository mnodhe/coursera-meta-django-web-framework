from django.db import models
from django.db import models

# Create your models here.

# let's add menu category to learn foreign key (one to many)


class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=200)


class Menu(models.Model):
    name = models.CharField(max_length=100)
    # category = models.CharField(max_length=100)
    # we need to change it to use foreign key
    category_id = models.ForeignKey(
        MenuCategory, on_delete=models.PROTECT, default=None, related_name="category_name")
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name + ' ' + self.cuisine


class Person(models.Model):
    person_name = models.CharField(max_length=20)
    person_age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)


# let's add some customer

class Customer(models.Model):
    name = models.CharField(max_length=200)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def __str__(self):
        return self.name
