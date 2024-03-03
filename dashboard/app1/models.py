from django.db import models

# Create your models here.


class user(models.Model):
    firstname= models.CharField( max_length=50)
    lastname= models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    username=models.CharField( max_length=50)
    password= models.CharField(max_length=50)
    cpassword= models.CharField( max_length=50)
    line1= models.CharField(max_length=50)
    city=models.CharField( max_length=50)
    state = models.CharField( max_length=50)
    pincode=models.IntegerField()
    pphoto=models.ImageField( upload_to="images")
    usertype=models.CharField(max_length=50)

