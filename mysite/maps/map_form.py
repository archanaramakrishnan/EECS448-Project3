from django.forms import ModelForm
from .models import Building
"""
class MapForm(ModelForm):
    class Meta:
        model=Map
        fields=['building1', 'building2']
"""
class BuildingForm(ModelForm):
    class Meta:
        model=Building
        fields=['name', 'latitude', 'longitude']