# Generated by Django 2.2 on 2020-12-11 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de Acceso', max_length=191)),
                ('slug', models.CharField(help_text='Ruta Amigable Acceso', max_length=191)),
                ('descripcion', models.CharField(blank=True, help_text='Descripción de Acceso', max_length=191, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creada', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificada', models.DateTimeField(auto_now=True)),
                ('fecha_eliminada', models.DateTimeField(blank=True, help_text='Fecha Eliminada', null=True)),
            ],
            options={
                'verbose_name_plural': 'accesos',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del Menú', max_length=191)),
                ('enlace', models.CharField(help_text='Ruta Menú', max_length=191)),
                ('icono', models.CharField(blank=True, help_text='Icono del Menú', max_length=191, null=True)),
                ('padre', models.IntegerField(default=0, help_text='Padre del Menú')),
                ('orden', models.SmallIntegerField(blank=True, help_text='Orden de menú', null=True)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creada', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificada', models.DateTimeField(auto_now=True)),
                ('fecha_eliminada', models.DateTimeField(blank=True, help_text='Fecha Eliminada', null=True)),
            ],
            options={
                'verbose_name_plural': 'menus',
            },
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de Acceso', max_length=191)),
                ('slug', models.CharField(help_text='Ruta Amigable Acceso', max_length=191)),
                ('descripcion', models.CharField(blank=True, help_text='Descripción de Acceso', max_length=191, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creada', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificada', models.DateTimeField(auto_now=True)),
                ('fecha_eliminada', models.DateTimeField(blank=True, help_text='Fecha Eliminada', null=True)),
            ],
            options={
                'verbose_name_plural': 'permisos',
            },
        ),
        migrations.AddField(
            model_name='usuario',
            name='empresa',
            field=models.ForeignKey(blank=True, help_text='Persona Usuario', null=True, on_delete=django.db.models.deletion.CASCADE, to='emp.Empresa'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, help_text='Nombre de Rol', max_length=191, null=True)),
                ('slug', models.CharField(blank=True, help_text='Ruta Amigable Rol', max_length=191, null=True)),
                ('descripcion', models.CharField(blank=True, help_text='Descripción de Rol', max_length=191, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creada', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificada', models.DateTimeField(auto_now=True)),
                ('fecha_eliminada', models.DateTimeField(blank=True, help_text='Fecha Eliminada', null=True)),
                ('acceso', models.ForeignKey(blank=True, help_text='Persona Usuario', null=True, on_delete=django.db.models.deletion.CASCADE, to='cuenta.Acceso')),
                ('menus', models.ManyToManyField(to='cuenta.Menu')),
                ('permisos', models.ManyToManyField(to='cuenta.Permiso')),
            ],
            options={
                'verbose_name_plural': 'roles',
            },
        ),
        migrations.AddField(
            model_name='usuario',
            name='roles',
            field=models.ManyToManyField(to='cuenta.Role'),
        ),
    ]
