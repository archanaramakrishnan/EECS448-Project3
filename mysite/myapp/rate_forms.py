from django import forms

from .models import Rate

class RateForm(forms.ModelForm):

    class Meta:
        model = Rate
        fields = ('class_rated', 'class_difficulty_level',)
