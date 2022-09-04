from django.db import models

# Create your models here.

class Products(models.Model):
    book=models.IntegerField()
    pen=models.IntegerField()
    notes=models.IntegerField()
    pencil=models.IntegerField()
    paper=models.IntegerField()
    