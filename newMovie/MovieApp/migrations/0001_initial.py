# Generated by Django 5.0.1 on 2024-03-12 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('director', models.CharField(blank=True, max_length=100)),
                ('release_year', models.CharField(blank=True, max_length=50)),
                ('budget', models.CharField(blank=True, max_length=50)),
                ('runtime', models.CharField(blank=True, max_length=50)),
                ('rating', models.CharField(blank=True, max_length=50)),
                ('genre', models.CharField(blank=True, max_length=50)),
                ('image_url', models.URLField(blank=True)),
                ('youtube_url', models.URLField(blank=True)),
            ],
        ),
    ]