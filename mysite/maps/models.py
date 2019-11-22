from django.db import models
from django.forms import ModelForm
from haversine import haversine
"""
BUILDING = [
    ('budig', 'Budig Hall'),
    ('wescoe', 'Wescoe Hall'),
    ('snow', 'Snow Hall'),
    ('leep', 'LEEP2'),
    ('learned', 'Learned Hall'),
    ('eaton', 'Eaton Hall'),
]
"""

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

BUILDING=list([building.name, building.name] for building in Building.objects.all())

# Create your models here.
class Map(models.Model):
    building1=models.CharField(max_length=255, choices=BUILDING, blank=False)
    building2=models.CharField(max_length=255, choices=BUILDING, blank=False)
    building3=models.CharField(max_length=255, choices=BUILDING, blank=True)
    building4=models.CharField(max_length=255, choices=BUILDING, blank=True)
    building5=models.CharField(max_length=255, choices=BUILDING, blank=True)

    def __str__(self):
        return '%s' % self.building1

class MapForm(ModelForm):
    class Meta:
        model = Map
        fields = ['building1', 'building2', 'building3', 'building4', 'building5']