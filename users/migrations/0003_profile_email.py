# Generated by Django 3.0.3 on 2020-11-01 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200824_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=200, null=True, unique=True),
        ),
    ]