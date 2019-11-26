from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    user_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #like_count= models.IntegerField(default=0)
    #counter= models.IntegerField(default=1)
    #likes= models.ManyToManyField('self',related_name = 'likes', blank = 'true')
    #FRESHMAN = 'FR'
    #SOPHOMORE = 'SP'
    #JUNIOR = 'JR'
    #SENIOR = 'SR'
    #GRADUATE = 'GR'
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
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


"""
class Like(models.Model):
    post= models.ForeignKey(Post, on_delete=models.DO_NOTHING,)
    value= models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    #class Meta:
       #unique_together = ("post", "value")
"""

class Rate(models.Model):

        CLASS_RATED = [('EECS101','EECS 101'),
                ('EECS168','EECS 168'),
                ('EECS140','EECS 140'),
                ('EECS210','EECS 210'),
                ('EECS268','EECS 268'),]

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
