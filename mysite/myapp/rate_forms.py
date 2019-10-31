from django import forms

class RateForm(forms.Form):

        class_rated = forms.ChoiceField(label ='Class you want to rate',
        choices = [('EECS101','EECS 101'),
                ('EECS168','EECS 168'),
                ('EECS140','EECS 140'),
                ('EECS210','EECS 210'),
                ('EECS268','EECS 268')])

        #rater_name = forms.CharField(max_length=30, label='What is your name?:')


        class_difficulty_level = forms.ChoiceField(choices= [('one','Super Easy'),
                                                            ('two','Easy'),
                                                            ('three','Average'),
                                                            ('four','Hard'),
                                                            ('five','Super Hard')])

        class_hours_spent = forms.ChoiceField(label='Weekly workload in hours:',
        choices = [('choice1','0 to 3'),
                ('choice2','3 to 6'),
                ('choice3','6 to 19'),
                ('choice4','9 to 12'),
                ('choice5','over 12')])

        rater_grade = forms.ChoiceField(label='What grade did you get in the class',
        choices = [('g0','Prefer not to disclose'),
                ('g1','Fail or drop'),
                ('g2','D'),
                ('g3','C'),
                ('g4','B'),
                ('g5','A')])

        class_exams_num = forms.IntegerField(max_value=10, label='How many exams was there?:')

        class_hw = forms.CharField(max_length=50, label='Comments about the HW (up to 50 characters):')

        class_comments = forms.CharField(max_length=300, label='Overall Comments (up to 300 characters):')

        class_overall = forms.ChoiceField(label='Overall message to freshman:',choices= [('one','I am so sorry for you'),
                                                            ('two','Get ready for a hard semester'),
                                                            ('three','You will be fine'),
                                                            ('four','Interesting class'),
                                                            ('five','Best class ever')])
