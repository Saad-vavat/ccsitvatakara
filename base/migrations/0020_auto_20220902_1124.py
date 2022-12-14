# Generated by Django 3.2.15 on 2022-09-02 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_delete_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrevQp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qp', models.FileField(upload_to='question paper')),
            ],
        ),
        migrations.CreateModel(
            name='QpLink',
            fields=[
                ('qp_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_name', models.CharField(max_length=120)),
                ('qp_year', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
        migrations.AddField(
            model_name='prevqp',
            name='qp_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.qplink'),
        ),
    ]
