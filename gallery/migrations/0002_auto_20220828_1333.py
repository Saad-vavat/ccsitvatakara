# Generated by Django 3.2.15 on 2022-08-28 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='event_name',
        ),
        migrations.DeleteModel(
            name='eventName',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
    ]