from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class AskInstance (models.Model):

    ask = models.ForeignKey('ask', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete= models.PROTECT )
    STATUS_CHOICES = (
        ('c', 'closed'),
        ('o', 'open'),
        ('f', 'freeze'),
    )
    status = models.CharField(max_length=256, choices=STATUS_CHOICES, default= 'o')


class Ask (models.Model):
    title = models.CharField( max_length = 256 )
    text = models.CharField( max_length = 256 )
    tags = models.ManyToManyField('Tags' ,blank=True)
    answers = models.ManyToManyField('Answer',blank=True)
    countLike = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return f"{self.title} {self.text} {self.tags} "


class Tags (models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.name}"




class AsksManager(models.Manager):
    def alive (self):
        return self.filter (death_date__isnull = True)


class Answer (models.Model):
    text = models.CharField(max_length=256)
    countLike = models.IntegerField(default=0,blank=True)
    is_correct = models.BooleanField(default=False)

    objects = AsksManager()

    def __str__(self):
        return f"{self.text} {self.is_correct}"

