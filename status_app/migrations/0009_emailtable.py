# Generated by Django 4.1.7 on 2023-06-27 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status_app', '0008_statustable8196_statustable8197_statustable8198'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emailtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmailInModel', models.EmailField(max_length=100)),
            ],
        ),
    ]
