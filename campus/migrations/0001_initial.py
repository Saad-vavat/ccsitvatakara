# Generated by Django 3.2.15 on 2022-09-02 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='video_or_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='campus_image')),
                ('video', models.FileField(null=True, upload_to='campus_video')),
            ],
        ),
    ]
