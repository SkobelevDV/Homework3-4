from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class AuthorManager(models.Manager):
    def alive (self):
        return self.filter (death_date__isnull = True)

class Genre (models.Model):
    name = models.CharField(max_length=256 , unique=True)

    def __str__(self):
        return f"{self.name}"
class Book (models.Model):
    title = models.CharField( max_length = 256 )
    author = models.ForeignKey('Author',max_length=256, on_delete= models.PROTECT)

    date_written = models.DateField(null= True, blank= True )

    genre = models.ManyToManyField('Genre')
    def __str__(self):
        return f"{self.title} {self.author} {self.genre} "

class Author (models.Model):
    name = models.CharField (max_length= 256)
    surname = models.CharField(max_length=256)
    birth_date = models.DateField()
    death_date = models.DateField(null=True, blank= True)
    is_deleted = models.BooleanField(default=False)

    objects = AuthorManager()

    def __str__(self):
        return f"{self.name} {self.surname}"

class BookInstance (models.Model):
    book = models.ForeignKey('book', on_delete=models.PROTECT )
    user = models.ForeignKey(User, on_delete= models.PROTECT )
    STATUS_CHOICES = (
        ('m', 'Maintenance'),
        ('a', 'Avaliiable'),
        ('t', 'Taken'),
    )
    status = models.CharField(max_length=256, choices=STATUS_CHOICES, default= 'm')
    due_date = models.DateField(null=True, blank=True)
