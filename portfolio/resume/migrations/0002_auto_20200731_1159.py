# Generated by Django 3.0.8 on 2020-07-31 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FilePathField(default='BhavnaSoni.png', path='resume/images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(default='https://github.com/bhavnas23'),
        ),
    ]
