# Generated by Django 3.2.7 on 2021-11-05 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0006_auto_20211102_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='rol',
            field=models.CharField(default='Estudiante', max_length=50),
        ),
        migrations.AddField(
            model_name='profesor',
            name='rol',
            field=models.CharField(default='Profesor', max_length=50),
        ),
    ]
