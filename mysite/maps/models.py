from django.db import models
from django.forms import ModelForm

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

# Create your models here.
class Map(models.Model):
    building1=models.CharField(max_length=255, choices=BUILDING)
    building2=models.CharField(max_length=255, choices=BUILDING)
    building3=models.CharField(max_length=255, choices=BUILDING)
    building4=models.CharField(max_length=255, choices=BUILDING)
    building5=models.CharField(max_length=255, choices=BUILDING)

    def __str__(self):
        return '%s' % self.building1

class MapForm(ModelForm):
    class Meta:
        model = Map
        fields = ['building1', 'building2', 'building3', 'building4', 'building5']