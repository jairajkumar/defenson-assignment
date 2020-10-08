from django.db import models

# Create your models here.
class Information(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    count = models.CharField(max_length=13)
    radio = models.CharField(max_length=13)
    

    date = models.DateField()

    def __str__(self):
        return (self.name)

# Create your models here.
