# Generated by Django 5.0.4 on 2024-08-22 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_tarea_financiera_tf_ccodigo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacion_empleado_contratista_tarea_financiera',
            name='AEC_COSTO_REAL',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Costo Real'),
        ),
        migrations.AddField(
            model_name='asignacion_empleado_contratista_tarea_financiera',
            name='AEC_HORAS_REALES',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Horas Reales'),
        ),
        migrations.AddField(
            model_name='asignacion_empleado_contratista_tarea_general',
            name='AEC_COSTO_REAL',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Costo Real'),
        ),
        migrations.AddField(
            model_name='asignacion_empleado_contratista_tarea_general',
            name='AEC_HORAS_REALES',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Horas Reales'),
        ),
        migrations.AddField(
            model_name='asignacion_empleado_contratista_tarea_ingenieria',
            name='AEC_COSTO_REAL',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Costo Real'),
        ),
        migrations.AddField(
            model_name='asignacion_empleado_contratista_tarea_ingenieria',
            name='AEC_HORAS_REALES',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Horas Reales'),
        ),
        migrations.AddField(
            model_name='asignacion_empleado_tarea_financiera',
            name='AE_COSTO_REAL',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Costo Real'),
        ),
        migrations.AddField(
            model_name='asignacion_empleado_tarea_financiera',
            name='AE_HORAS_REALES',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Horas Reales'),
        ),
        migrations.AddField(
            model_name='asignacion_empleado_tarea_general',
            name='AE_COSTO_REAL',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Costo Real'),
        ),
        migrations.AddField(
            model_name='asignacion_empleado_tarea_general',
            name='AE_HORAS_REALES',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Horas Reales'),
        ),
        migrations.AddField(
            model_name='asignacion_empleado_tarea_ingenieria',
            name='AE_COSTO_REAL',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Costo Real'),
        ),
        migrations.AddField(
            model_name='asignacion_empleado_tarea_ingenieria',
            name='AE_HORAS_REALES',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Horas Reales'),
        ),
        migrations.AddField(
            model_name='asignacion_recurso_tarea_financiera',
            name='ART_COSTO_REAL',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Costo Real'),
        ),
        migrations.AddField(
            model_name='asignacion_recurso_tarea_financiera',
            name='ART_HORAS_REALES',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Horas Reales'),
        ),
        migrations.AddField(
            model_name='asignacion_recurso_tarea_general',
            name='ART_COSTO_REAL',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Costo Real'),
        ),
        migrations.AddField(
            model_name='asignacion_recurso_tarea_general',
            name='ART_HORAS_REALES',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Horas Reales'),
        ),
        migrations.AddField(
            model_name='asignacion_recurso_tarea_ingenieria',
            name='ART_COSTO_REAL',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Costo Real'),
        ),
        migrations.AddField(
            model_name='asignacion_recurso_tarea_ingenieria',
            name='ART_HORAS_REALES',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Horas Reales'),
        ),
    ]
