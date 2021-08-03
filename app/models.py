from django.db import models
from django.db.models.base import Model

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
            
        return  False
    
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


class Restaurant(models.Model):
    RestaurantNmame = models.CharField(max_length=100)
    phoneno = models.IntegerField(max_length=12)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.RestaurantNmame

class Item(models.Model):
    ItemName = models.CharField(max_length=100)

    def __str__(self):
        return self.ItemName
    
class Menu(models.Model):
    RestaurantName = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    ItemName = models.ForeignKey(Item,on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

class Order(models.Model):
    username = models.CharField(max_length=100)
    itemname = models.CharField(max_length=100)
    restaurant = models.CharField(max_length=100,default=None)
    price = models.IntegerField()
    phoneno = models.CharField(max_length=12)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.username