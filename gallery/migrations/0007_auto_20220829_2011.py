# Generated by Django 3.2.15 on 2022-08-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_alter_category_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='category',
            new_name='images',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='categories',
            field=models.ImageField(default=True, upload_to='category_images'),
            preserve_default=False,
        ),
    ]
