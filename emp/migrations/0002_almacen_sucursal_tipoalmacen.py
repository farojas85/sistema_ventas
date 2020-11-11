# Generated by Django 2.2 on 2020-11-11 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
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
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=191)),
                ('direccion', models.CharField(max_length=191)),
                ('referencia', models.CharField(blank=True, max_length=191, null=True)),
                ('observacion', models.CharField(blank=True, max_length=191, null=True)),
                ('area', models.CharField(blank=True, max_length=191, null=True)),
                ('sucursal', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.Sucursal')),
                ('tipo_almacen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.TipoAlmacen')),
                ('ubigeo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.Distrito')),
            ],
            options={
                'verbose_name_plural': 'Almacenes',
            },
        ),
    ]
