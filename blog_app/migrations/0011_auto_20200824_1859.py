# Generated by Django 3.0.3 on 2020-08-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0010_auto_20200822_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
