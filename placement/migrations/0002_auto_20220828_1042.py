# Generated by Django 3.2.15 on 2022-08-28 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='company_logo',
            field=models.ImageField(upload_to='placement'),
        ),
        migrations.AlterField(
            model_name='placement',
            name='image',
            field=models.ImageField(upload_to='placement'),
        ),
    ]
