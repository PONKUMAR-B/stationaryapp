from django.db import models

# Create your models here.

class Products(models.Model):
    month=models.CharField(max_length=100,default='')
    book=models.IntegerField()
    pen=models.IntegerField()
    notes=models.IntegerField()
    pencil=models.IntegerField()
    paper=models.IntegerField()
