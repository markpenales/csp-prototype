# Generated by Django 4.2.6 on 2023-10-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laboratory',
            name='course',
            field=models.TextField(),
        ),
    ]
