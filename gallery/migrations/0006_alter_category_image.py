# Generated by Django 3.2.15 on 2022-08-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20220829_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='category_wise_images'),
        ),
    ]