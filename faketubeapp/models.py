from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Video(models.Model):
    FUNC_CHOICES=(
        ('Music','Music'),
        ('Entertainment','Entertainment'),
        ('Education','Education'),
        ('Kitties','Kitties'),
        ('Doggos','Doggos')

    )
        

    title=models.CharField(max_length=200)
    thumbs_up=models.IntegerField(default=0)
    thumbs_down=models.IntegerField(default=0)
    theme=models.CharField(max_length=100,choices=FUNC_CHOICES)
