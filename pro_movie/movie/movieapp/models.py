from django.db import models

# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=250)
    year = models.IntegerField()
    image = models.ImageField(upload_to='photos')
    description = models.TextField()


    def __str__(self):
         return self.name