# Generated by Django 3.2.15 on 2022-08-28 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('batch', models.IntegerField()),
                ('placed_at', models.CharField(max_length=100)),
                ('company_logo', models.ImageField(upload_to='')),
            ],
        ),
    ]
