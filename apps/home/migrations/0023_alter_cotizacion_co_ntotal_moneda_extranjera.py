# Generated by Django 5.0.4 on 2024-09-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_alter_tipo_cambio_tc_ffecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotizacion',
            name='CO_NTOTAL_MONEDA_EXTRANJERA',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=15, null=True, verbose_name='Total en Moneda Extranjera'),
        ),
    ]
