# Generated by Django 3.0.3 on 2020-08-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20200805_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_updated',
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
