# Generated by Django 2.2 on 2020-11-17 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=191)),
                ('direccion', models.CharField(max_length=191)),
                ('area', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True)),
                ('capacidad', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True)),
            ],
            options={
                'verbose_name_plural': 'Almacenes',
            },
        ),
        migrations.CreateModel(
            name='TipoAlmacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(blank=True, max_length=191, null=True)),
            ],
            options={
                'verbose_name_plural': 'TipoAlmacenes',
            },
        ),
        migrations.CreateModel(
            name='TipoEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(help_text='Codigo Tipo Empresa', max_length=2)),
                ('nombre', models.CharField(help_text='Descripción de Tipo Empresa', max_length=191)),
                ('comentario', models.CharField(help_text='Comentario de Tipo Empresa', max_length=191)),
            ],
            options={
                'verbose_name_plural': 'TipoEmpresas',
            },
        ),
        migrations.CreateModel(
            name='TipoPuntoVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(blank=True, max_length=191, null=True)),
            ],
            options={
                'verbose_name_plural': 'TipoPuntoVentas',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('id_sunat', models.CharField(blank=True, max_length=10, null=True)),
                ('nombre', models.CharField(blank=True, max_length=191, null=True)),
                ('impresion', models.CharField(blank=True, max_length=191, null=True)),
            ],
            options={
                'verbose_name_plural': 'UnidadMedidas',
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=191)),
                ('direccion', models.CharField(max_length=191)),
                ('referencia', models.CharField(blank=True, max_length=191, null=True)),
                ('observacion', models.CharField(blank=True, max_length=191, null=True)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.Empresa')),
                ('ubigeo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.Distrito')),
            ],
            options={
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.CreateModel(
            name='PuntoVenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre_equipo', models.CharField(max_length=191)),
                ('almacen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.Almacen')),
                ('tipo_punto_venta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.TipoPuntoVenta')),
            ],
            options={
                'verbose_name_plural': 'PuntoVentas',
            },
        ),
        migrations.AddField(
            model_name='almacen',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.Sucursal'),
        ),
        migrations.AddField(
            model_name='almacen',
            name='tipo_almacen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.TipoAlmacen'),
        ),
        migrations.AddField(
            model_name='almacen',
            name='ubigeo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.Distrito'),
        ),
        migrations.AddField(
            model_name='almacen',
            name='unidad_medidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.UnidadMedida'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='tipo_empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.TipoEmpresa'),
        ),
    ]
