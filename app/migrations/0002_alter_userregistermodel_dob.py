# Generated by Django 3.2 on 2021-04-13 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistermodel',
            name='DOB',
            field=models.DateField(),
        ),
    ]
