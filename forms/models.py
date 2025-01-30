from django.db import models

# Create your models here.
class Detail(models.Model):
    name=models.CharField(max_length=50)
    phno=models.CharField(max_length=50)
    email=models.EmailField(max_length=250)
    addr=models.TextField()