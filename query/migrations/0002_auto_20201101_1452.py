# Generated by Django 3.1.2 on 2020-11-01 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('query', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='location',
            name='location_category',
        ),
        migrations.RemoveField(
            model_name='location',
            name='till_date',
        ),
    ]