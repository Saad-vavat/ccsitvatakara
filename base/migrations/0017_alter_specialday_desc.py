# Generated by Django 3.2.15 on 2022-08-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_specialday_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialday',
            name='desc',
            field=models.CharField(blank=True, default=True, max_length=20),
            preserve_default=False,
        ),
    ]
