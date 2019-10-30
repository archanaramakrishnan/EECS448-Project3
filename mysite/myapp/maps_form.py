from django import forms

class mapsForm(forms.Form):
    building = forms.ChoiceField(choices=[('leep', 'LEEP2'),
                                        ('eaton', 'Eaton Hall'),
                                        ('learned', 'Learned Hall'),
                                        ('slawson', 'Slawson Hall'),
                                        ('budig', 'Budig Hall')
                                       ])
    

