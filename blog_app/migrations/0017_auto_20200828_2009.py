# Generated by Django 3.0.3 on 2020-08-28 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0016_auto_20200828_0702'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog_app.Comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='published', max_length=10),
        ),
    ]
