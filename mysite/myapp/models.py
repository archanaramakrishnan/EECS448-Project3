from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Rate(models.Model):
    CLASS_RATED = [('EECS101','EECS 101'),
            ('EECS168','EECS 168'),
            ('EECS140','EECS 140'),
            ('EECS210','EECS 210'),
            ('EECS268','EECS 268'),]

    class_rated = models.CharField(
        max_length=20,
        choices=CLASS_RATED,
        default='EECS101',
    )

    CLASS_DIFFICULTY_LEVEL = [('one','Super Easy'),
                            ('two','Easy'),
                            ('three','Average'),
                            ('four','Hard'),
                            ('five','Super Hard'),]

    class_difficulty_level = models.CharField(
        max_length=20,
        choices=CLASS_DIFFICULTY_LEVEL,
        default='one',
    )
