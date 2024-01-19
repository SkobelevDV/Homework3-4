from django.core.management.base import BaseCommand
from app.models import *


class Command(BaseCommand):
    help = 'Очистить базу данных'

    def handle(self, *args, **options):
        Answer.objects.all().delete()
        Question.objects.all().delete()
        Tag.objects.all().delete()
        LikeQuestion.objects.all().delete()
        LikeAnswer.objects.all().delete()
        Profile.objects.all().delete()