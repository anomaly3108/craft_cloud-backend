from django.db import models

class testdata(models.Model):
    name=models.CharField(max_length=10)
    class Meta:
        db_table='test'

class displaydata(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    class Meta:
        db_table='display'