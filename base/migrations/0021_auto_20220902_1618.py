# Generated by Django 3.2.15 on 2022-09-02 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_auto_20220902_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qpaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qp', models.FileField(upload_to='question_paer')),
            ],
        ),
        migrations.RenameField(
            model_name='qplink',
            old_name='qp_year',
            new_name='year_of_qp',
        ),
        migrations.DeleteModel(
            name='PrevQp',
        ),
        migrations.AddField(
            model_name='qpaper',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.qplink'),
        ),
    ]
