# Generated by Django 5.0.1 on 2024-02-21 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('image_url', models.URLField()),
                ('image_classpath', models.CharField(max_length=255)),
                ('youtube_link', models.URLField()),
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('director', models.CharField(max_length=255)),
                ('release_year', models.IntegerField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=14)),
                ('runtime', models.IntegerField()),
                ('rating', models.CharField(max_length=50)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='MovieTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('purchase_date', models.DateField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hw2_movieapp.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=100)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='hw2_movieapp.user')),
            ],
        ),
    ]
