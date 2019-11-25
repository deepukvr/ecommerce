from django.db import models

class Cart(models.Model):
    username=models.CharField(max_length=20)
    pid=models.IntegerField()
    units=models.IntegerField()
    unitprice=models.DecimalField(max_digits=10,decimal_places=4)
    tuprice=models.DecimalField(max_digits=10,decimal_places=4)


