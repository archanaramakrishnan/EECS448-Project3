from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    It is a model that stores infromation of advice posts made by students

    """
    user_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    likes= models.IntegerField(default=0)
    YEAR_IN_SCHOOL_CHOICES = [
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Graduate', 'Graduate'),
    ]

    year_in_school = models.CharField(
        max_length=9,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default='GRADUATE',


    )


    def publish(self):
        """Makes the posts live on the site."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class Preference(models.Model):
    post= models.ForeignKey(Post, on_delete=models.DO_NOTHING,)
    value= models.IntegerField()


    class Rate(models.Model):
        """
        It is a model that stores infromation needed to rate a class by a student

        """
        CLASS_RATED =[('EECS101','EECS 101'),
                        ('EECS168','EECS 168'),
                        ('EECS140','EECS 140'),
                        ('EECS210','EECS 210'),
                        ('EECS268','EECS 268'),
                        ('EECS368','EECS 368'),
                        ('EECS388','EECS 388'),
                        ('EECS448','EECS 448'),
                        ('EECS510','EECS 510'),
                        ('EECS560','EECS 560'),
                        ('MATH125','MATH 125'),
                        ('MATH126','MATH 126'),
                        ('MATH127','MATH 127'),
                        ('MATH290','MATH 290'),
                        ('PHSX210','PHSX 210'),
                        ('PHSX216','PHSX 216'),
                        ('PHSX212','PHSX 236'),]

        class_rated = models.CharField(
        max_length=20,
        choices=CLASS_RATED,
        default='EECS101',)

        CLASS_DIFFICULTY_LEVEL =  [('one','Super Easy'),
                                    ('two','Easy'),
                                    ('three','Average'),
                                    ('four','Hard'),
                                    ('five','Super Hard')]

        class_difficulty_level = models.CharField(
        max_length=20,
        choices=CLASS_DIFFICULTY_LEVEL,
        default='Super Easy',)

        CLASS_HOURS_SPENT =[('choice1','0 to 3'),
                ('choice2','3 to 6'),
                ('choice3','6 to 9'),
                ('choice4','9 to 12'),
                ('choice5','over 12')]

        class_hours_spent = models.CharField(
        max_length=20,
        choices=CLASS_HOURS_SPENT,
        default='0 to 3',)

        RATER_GRADE =[('g0','Prefer not to disclose'),
                ('g1','Fail or drop'),
                ('g2','D'),
                ('g3','C'),
                ('g4','B'),
                ('g5','A')]

        rater_grade = models.CharField(
        max_length=20,
        choices=RATER_GRADE,
        default='Prefer not to disclose',)

        class_exams_num = models.IntegerField()

        class_hw = models.CharField(max_length=50)

        class_comments = models.CharField(max_length=300)

        CLASS_OVERALL = [('one','I am so sorry for you'),
                        ('two','Get ready for a hard semester'),
                        ('three','You will be fine'),
                        ('four','Interesting class'),
                        ('five','Best class ever')]

        class_overall = models.CharField(
        max_length=20,
        choices=CLASS_OVERALL,
        default='I am so sorry for you',)
