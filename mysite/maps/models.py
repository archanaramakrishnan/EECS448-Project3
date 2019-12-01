from django.db import models
from django.forms import ModelForm
from haversine import haversine

class Building(models.Model):
    """
    A model that stores information of buildings on the KU campus

    """
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        """
        Returns the name of the building
        
        """
        return self.name

class BuildingForm(ModelForm):
    """
    A modelform that stores the latitude, longitude, and name of a building

    """
    class Meta:
        model = Building
        fields = ['name', 'latitude', 'longitude']

BUILDING=list([building.name, building.name] for building in Building.objects.all())

class Map(models.Model):
    """
    A model that stores information of 5 choices of buildings from the user, with the first two fields being required

    """
    building1=models.CharField(max_length=255, choices=BUILDING, blank=False)
    building2=models.CharField(max_length=255, choices=BUILDING, blank=False)
    building3=models.CharField(max_length=255, choices=BUILDING, blank=True)
    building4=models.CharField(max_length=255, choices=BUILDING, blank=True)
    building5=models.CharField(max_length=255, choices=BUILDING, blank=True)

    def __str__(self):
        """
        Returns the name of the first building chosen out of the 5 buildings
        """
        return '%s' % self.building1

class MapForm(ModelForm):
    """
    A modelform that has a 5 drop downs to choose buildings out of the ones stored in the Building class

    """
    class Meta:
        model = Map
        fields = ['building1', 'building2', 'building3', 'building4', 'building5']