# Generated by Django 2.2 on 2020-12-20 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0003_configuracionempresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=191, null=True, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('observacion', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Configuraciones',
            },
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='cantidad_precios',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='cantidad_resumen_boletas',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='cotizacion',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='descuento_global',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='descuento_item_pv',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='detalle_producto',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='dias_max_anulacion',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='direccion_envio_bf',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='direccion_envio_gr',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='direccion_envio_ncd',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='edicion_precios_pv',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='envio_xml_boletas',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='fecha_inicio_contrato',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='fecha_renovacion_contrato',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='moneda',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='mostrar_codigo_barras',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='mostrar_codigo_fabricante',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='mostrar_codigo_interno',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='mostrar_codigo_proveedor',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='mostrar_codigo_sunat',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='ose_sunat',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='placa_columna',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='precio_venta_independiente',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='producto_reemplazo',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='saldo_punto_venta',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='ubicacion_base_datos',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='ubicacion_exonerado',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='vales_producto_exclusivo',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='vales_producto_factura',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='vales_producto_nofactura',
        ),
        migrations.RemoveField(
            model_name='configuracionempresa',
            name='vales_salida_efectivo',
        ),
        migrations.AddField(
            model_name='configuracionempresa',
            name='valor',
            field=models.CharField(blank=True, max_length=191, null=True),
        ),
        migrations.AlterField(
            model_name='configuracionempresa',
            name='empresa',
            field=models.ForeignKey(blank=True, help_text='Modelo Empresa', null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.Empresa'),
        ),
        migrations.AddField(
            model_name='configuracionempresa',
            name='configuracion',
            field=models.ForeignKey(blank=True, help_text='Modelo Configuracion', null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.Configuracion'),
        ),
    ]