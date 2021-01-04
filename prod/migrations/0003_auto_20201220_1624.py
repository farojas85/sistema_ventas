# Generated by Django 2.2 on 2020-12-20 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prod', '0002_auto_20201211_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='detalle',
            field=models.TextField(blank=True, help_text='Detalle de Producto', max_length=500, null=True),
        ),
        migrations.CreateModel(
            name='ProductoPrecio',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, help_text='Precio Venta del Producto', max_digits=18)),
                ('estado', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='prod.Producto')),
            ],
        ),
    ]
