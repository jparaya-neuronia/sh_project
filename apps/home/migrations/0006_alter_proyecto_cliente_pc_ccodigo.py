# Generated by Django 5.0.4 on 2024-08-16 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_tarea_financiera_tf_proyecto_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto_cliente',
            name='PC_CCODIGO',
            field=models.CharField(max_length=100, unique=True, verbose_name='Código de proyecto'),
        ),
    ]
