# Generated by Django 4.1.7 on 2023-06-16 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status_app', '0004_statustabletwo'),
    ]

    operations = [
        migrations.AddField(
            model_name='statustabletwo',
            name='TagStatus8194',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statustabletwo',
            name='TagStatus8195',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statustabletwo',
            name='TagStatus8196',
            field=models.CharField(default='true', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statustabletwo',
            name='TagStatus8197',
            field=models.CharField(default='true', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statustabletwo',
            name='TagStatus8198',
            field=models.CharField(default='true', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statustabletwo',
            name='TagStatus8199',
            field=models.CharField(default='false', max_length=50),
            preserve_default=False,
        ),
    ]
