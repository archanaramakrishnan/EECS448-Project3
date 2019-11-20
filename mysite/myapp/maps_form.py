from django import forms

class mapsForm(forms.Form):
    building1 = forms.ChoiceField(choices=[('leep', 'LEEP2'),
                                        ('eaton', 'Eaton Hall'),
                                        ('learned', 'Learned Hall'),
                                        ('slawson', 'Slawson Hall'),
                                        ('budig', 'Budig Hall')
                                       ])

    building2 = forms.ChoiceField(choices=[('leep', 'LEEP2'),
                                        ('eaton', 'Eaton Hall'),
                                        ('learned', 'Learned Hall'),
                                        ('slawson', 'Slawson Hall'),
                                        ('budig', 'Budig Hall')
                                       ])

    building3 = forms.ChoiceField(choices=[('leep', 'LEEP2'),
                                        ('eaton', 'Eaton Hall'),
                                        ('learned', 'Learned Hall'),
                                        ('slawson', 'Slawson Hall'),
                                        ('budig', 'Budig Hall')
                                       ])

    building4 = forms.ChoiceField(choices=[('leep', 'LEEP2'),
                                        ('eaton', 'Eaton Hall'),
                                        ('learned', 'Learned Hall'),
                                        ('slawson', 'Slawson Hall'),
                                        ('budig', 'Budig Hall')
                                       ])
