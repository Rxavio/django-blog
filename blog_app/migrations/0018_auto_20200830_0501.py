# Generated by Django 3.0.3 on 2020-08-30 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0017_auto_20200828_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='published', max_length=10),
        ),
    ]