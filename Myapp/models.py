from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=200)
    passion= models.TextField()
    citizenship =models.CharField(max_length=100)

    def __str__(self) :
        return self.name