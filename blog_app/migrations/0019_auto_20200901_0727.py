# Generated by Django 3.0.3 on 2020-09-01 05:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_app', '0018_auto_20200830_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='published', max_length=10),
        ),
    ]
