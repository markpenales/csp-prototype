# Generated by Django 4.2.6 on 2023-10-15 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_alter_laboratory_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='time_end',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time_start',
            field=models.CharField(max_length=255),
        ),
    ]
