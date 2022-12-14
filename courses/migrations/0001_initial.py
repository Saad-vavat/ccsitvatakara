# Generated by Django 3.2.15 on 2022-08-27 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_image', models.ImageField(upload_to='course')),
                ('course_name', models.CharField(max_length=100)),
                ('course_brief', models.CharField(max_length=200)),
                ('cours_desc', models.TextField()),
            ],
        ),
    ]
