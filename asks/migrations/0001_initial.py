# Generated by Django 4.2.7 on 2024-01-12 23:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=256)),
                ('countLike', models.IntegerField()),
                ('is_correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('text', models.CharField(max_length=256)),
                ('countLike', models.IntegerField()),
                ('answers', models.ManyToManyField(to='asks.answer')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='AskInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('c', 'closed'), ('o', 'open'), ('f', 'freeze')], default='o', max_length=256)),
                ('ask', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='asks.ask')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ask',
            name='tags',
            field=models.ManyToManyField(to='asks.tags'),
        ),
    ]
