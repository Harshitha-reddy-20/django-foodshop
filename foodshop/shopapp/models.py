from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class fooditem(models.Model):
    name=models.CharField(max_length=50,verbose_name="Fooditem name")
    price=models.FloatField()
    fdetails=models.CharField(max_length=150,verbose_name="Description")
    CAT=((1,"Biryani"),(2,"Pizza"),(3,"Burger"),(4,"Desserts"),(5,"South Indian"))
    cat=models.IntegerField(verbose_name="Category",choices=CAT)
    is_active=models.BooleanField(default=True,verbose_name="Available")
    fimage=models.ImageField(upload_to='image')

    
class Cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    fid=models.ForeignKey(fooditem,on_delete=models.CASCADE,db_column="fid")
    qty=models.IntegerField(default=1)

class Order(models.Model):
    order_id=models.CharField(max_length=100)
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column="uid")
    fid=models.ForeignKey(fooditem,on_delete=models.CASCADE,db_column="fid")
    qty=models.IntegerField(default=1)






 