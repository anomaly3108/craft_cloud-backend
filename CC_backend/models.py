from django.db import models

class testdata(models.Model):
    name=models.CharField(max_length=10)
    class Meta:
        db_table='test'

class display_users(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    user_type=models.IntegerField
    objects = models.Manager()
    class Meta:
        db_table='users'


class user_rating(models.Model):
    user_id=models.CharField(max_length=10)
    star1=models.CharField(max_length=10)
    star2=models.CharField(max_length=10)
    star3=models.CharField(max_length=10)
    star4=models.CharField(max_length=10)
    star5=models.CharField(max_length=10)
    class Meta:
        db_table='ratings'

class displaypost(models.Model):
    user_id = models.CharField(max_length=50)
    post_title = models.CharField(max_length=50)
    post_desc = models.CharField(max_length=255)
    post_type = models.CharField(max_length=50)
    post_price = models.CharField(max_length=50)
    objects = models.Manager()
    class Meta:
        db_table='posts'