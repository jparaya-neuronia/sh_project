# Generated by Django 5.1 on 2024-09-04 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_unidad_negocio_un_ffecha_creacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unidad_negocio',
            options={'verbose_name': 'Unidad de Negocio', 'verbose_name_plural': 'Unidades de Negocio'},
        ),
        migrations.AlterModelTable(
            name='unidad_negocio',
            table='UNIDAD_NEGOCIO',
        ),
    ]
