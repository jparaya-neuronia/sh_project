# Generated by Django 2.1.15 on 2024-09-25 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0041_auto_20240925_1151'),
    ]

    operations = [

        migrations.AlterField(
            model_name='hh_control',
            name='HH_CONTROL_USER_ID',
            field=models.CharField(max_length=50),
        )
       
    ]
