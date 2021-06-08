from django.db import models

class user_type(models.Model):
    type_name=models.CharField(max_length=50)
    price=models.CharField(max_length=10)
    class Meta:
        db_table='type'

class login(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=250)
    user_type=models.CharField(max_length=50)
    class Meta:
        db_table='users'

class display_users(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    user_type=models.CharField(max_length=50)
    address=models.CharField(max_length=250)
    rating=models.CharField(max_length=50)
    class Meta:
        db_table='users','type'

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
    class Meta:
        db_table='posts'

class singlepost(models.Model):
    name=models.CharField(max_length=50)
    post_title = models.CharField(max_length=50)
    post_desc = models.CharField(max_length=255)
    post_type = models.CharField(max_length=50)
    post_price = models.CharField(max_length=50)
    class Meta:
        db_table= 'posts','users'

class orders(models.Model):
    user_id = models.CharField(max_length=50)
    post_title = models.CharField(max_length=50)
    post_desc = models.CharField(max_length=255)
    post_type = models.CharField(max_length=50)
    post_price = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
    pid = models.CharField(max_length=255)
    done = models.CharField(max_length=1)
    review = models.CharField(max_length=1)
    class Meta:
        db_table= 'posts','orders'

class add_order(models.Model):
    uid = models.CharField(max_length=50)
    pid = models.CharField(max_length=50)
    sid = models.CharField(max_length=50)
    class Meta:
        db_table='orders'

class user_wallet(models.Model):
    uid=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)
    class Meta:
        db_table='wallet_transaction'