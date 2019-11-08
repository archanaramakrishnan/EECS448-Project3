from django.db import models
from django.forms import ModelForm

"""
# Create your models here.
class Map(models.Model):
    building1=models.CharField(max_length=255)
    building2=models.CharField(max_length=255, default='')

    def __str__(self):
        return '%s' % self.building1
"""
BUILDING = [
    ('budig', 'Budig Hall'),
    ('wescoe', 'Wescoe Hall'),
    ('snow', 'Snow Hall'),
    ('leep', 'LEEP2'),
    ('learned', 'Learned Hall'),
    ('eaton', 'Eaton Hall'),
]

class Building(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class BuildingForm(ModelForm):
    class Meta:
        model = Building
        fields = ['name', 'latitude', 'longitude']