# Generated by Django 3.0.7 on 2020-07-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local_app', '0016_auto_20200703_0341'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedpin',
            name='image_2',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='savedpin',
            name='image_3',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
