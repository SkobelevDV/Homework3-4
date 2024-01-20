import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, BaseUserManager, User
from django.db.models import Count, Q
from django.utils import timezone


class LikeManager(models.Manager):
    pass


class QuestionManager(models.Manager):
    def few_best_questions(self, amount=10):
        return self.all().order_by('-total_likes')[:amount]

    def hot_questions(self, amount=10):
        return self.all().order_by('-total_likes', '-total_answers')[:amount]

    def this_tag_questions(self, tag_id):
        tag = Tag.objects.get(id=tag_id)
        return self.get_queryset().filter(tags=tag).order_by('-id')

    def newest_questions(self, amount=10):
        return self.all().order_by('-date_written')[:amount]


class TagManager(models.Manager):
    def top_tags(self, count_top=7):
        # топ 7 тегов из базы данных (самых популярных)
        popular_tags = self.annotate(num_questions=Count('questions')).order_by('-num_questions')[:count_top]
        return popular_tags

class ProfileManager(BaseUserManager):
    def best_users(self, amount):
        print(self.annotate(correct_answers_count=Count('answer', filter=Q(answer__is_correct=True))).order_by(
                '-correct_answers_count')[:amount])
        return self.annotate(correct_answers_count=Count('answer', filter=Q(answer__is_correct=True))).order_by(
                '-correct_answers_count')[:amount]


class AnswerManager(models.Manager):
    def correct(self):
        return self.filter(is_correct=True)

    def not_correct(self):
        return self.filter(is_correct=False)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    objects = TagManager()

    def __str__(self):
        return f"{self.name}"

class Profile(models.Model):
    userAuth = models.OneToOneField(User, on_delete=models.CASCADE, default= User)
    nickname = models.CharField('User Nickname', max_length=50, default='user')
    photo = models.ImageField(null=True, blank=True, default="img/fiona.png")
    groups = models.ManyToManyField(Group, related_name="custom_user_set")
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_set")

    objects = ProfileManager()
    def __str__(self):
        return f"{self.nickname}"

class Question(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=False)
    photo = models.ImageField(upload_to="img/")
    tags = models.ManyToManyField(Tag, related_name='questions')
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    date_written = models.DateTimeField(default=timezone.now)
    total_likes = models.IntegerField(default=0)
    total_answers = models.IntegerField(default=0)

    objects = QuestionManager()

    def __str__(self):
        return f"{self.title}"

class Answer(models.Model):
    content = models.TextField(blank=False)
    is_correct = models.BooleanField(blank=True)
    what_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    date_written = models.DateTimeField(default=timezone.now)
    total_likes = models.IntegerField(default=0)

    objects = AnswerManager()

    def __str__(self):
        return f"{self.content[:30]}..."

class LikeQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, default=None)
    type = models.IntegerField(default=0)  # 1 like, -1 dislike, 0 ignore
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)

    class Meta:
        unique_together = ('question', 'author')  # Ensure one user can give at most one like/dislike to a question

    objects = LikeManager()

    def __str__(self):
        return f'Like from user: {self.author}, to question {self.question}'

class LikeAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, default=None)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    type = models.IntegerField(default=0)  # 1 like, -1 dislike, 0 ignore

    objects = LikeManager()

    class Meta:
        unique_together = ('answer', 'author')  # Ensure one user can give at most one like/dislike to an answer

    def __str__(self):
        return f'Like from user: {self.author}, to answer {self.answer}'

