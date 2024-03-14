from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=1287)
    title = models.CharField(max_length=56)
    author = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField()
    quantity = models.IntegerField()

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, default="")
    cellPhoneNumber = models.CharField(max_length=12)


class Rent(models.Model):
    id = models.AutoField(primary_key=True)
    rentStart = models.DateTimeField(null=True,blank=True)
    rentEnd = models.DateTimeField(null=True,blank=True)
    status = models.CharField(max_length=25,null=True,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

