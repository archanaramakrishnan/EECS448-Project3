from django import forms
from .models import Rate


class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('class_rated', 'class_difficulty_level','class_hours_spent','rater_grade',
        'class_exams_num', 'class_hw', 'class_comments', 'class_overall')
