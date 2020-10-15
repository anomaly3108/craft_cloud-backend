from django.db import models

class testdata(models.Model):
    name=models.CharField(max_length=10)
    class Meta:
        db_table='test'