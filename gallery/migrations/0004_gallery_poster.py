# Generated by Django 3.2.15 on 2022-08-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_category_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='poster',
            field=models.ImageField(default=True, upload_to='gallery'),
            preserve_default=False,
        ),
    ]
