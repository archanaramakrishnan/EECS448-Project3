from django.db import models

# Create your models here.
class Map(models.Model):
    building1=models.CharField(max_length=255)
    building2=models.CharField(max_length=255, default='')

    def __str__(self):
        return '%s' % self.building1