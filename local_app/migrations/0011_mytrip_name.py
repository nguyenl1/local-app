# Generated by Django 3.0.7 on 2020-06-30 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local_app', '0010_submitpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytrip',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
