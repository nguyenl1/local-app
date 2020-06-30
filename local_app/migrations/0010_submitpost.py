# Generated by Django 3.0.7 on 2020-06-29 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local_app', '0009_auto_20200625_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('zip_code', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, max_length=200)),
                ('publisher_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]