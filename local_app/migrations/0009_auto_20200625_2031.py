# Generated by Django 3.0.7 on 2020-06-26 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local_app', '0008_savedpin_coordinates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savedpin',
            old_name='coordinates',
            new_name='latitude',
        ),
        migrations.AddField(
            model_name='savedpin',
            name='city',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='savedpin',
            name='longitude',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='savedpin',
            name='state',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='savedpin',
            name='zip_code',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='savedpin',
            name='address',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
