# Generated by Django 2.2 on 2020-12-20 21:44

from django.db import models,migrations

class ConfiguracionesDatos:
    @classmethod
    def cargar_datos(cls,apps,schema_editor):
        db_alias = schema_editor.connection.alias
        
        Configuracion = apps.get_model('emp','Configuracion')
        
        cls.configuracion1, created = Configuracion.objects.get_or_create(
            nombre='Ocultar Columna Saldo Punto de Venta',descripcion='Oculta la columna Saldo de Productos en el punto de Venta',
            observacion='0 - Oculta. 1 - Muestra')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion1.id))

        cls.configuracion2, created = Configuracion.objects.get_or_create(
            nombre='Permitir detalle de Producto',descripcion='Activa la opción de escribir el detalle para los productos que  requieran usar la columna detalle de la tabla produto',
            observacion='0 - Desactivado. 1 - Activado')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion2.id))

        cls.configuracion3, created = Configuracion.objects.get_or_create(
            nombre='Permitir descuentos por item en el punto de Venta',descripcion='Oculta la columna de descuento por Item en el punto de venta',
            observacion='0 - Oculta. 1 - Muestra')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion3.id))

        cls.configuracion4, created = Configuracion.objects.get_or_create(
            nombre='Permitir Descuento Global',descripcion='Bloquea la opción de editar el monto de descuento',
            observacion='0 - Bloqueado. 1 - Habilitado')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion4.id))

        cls.configuracion5, created = Configuracion.objects.get_or_create(
            nombre='Permitir Edición de los precios en los puntos de Venta',descripcion='Permite la edición de precios en los puntos de Venta',
            observacion='0 - Bloquea Edición. 1 - Permite Edición')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion5.id))

        cls.configuracion6, created = Configuracion.objects.get_or_create(
            nombre='Cantidad de Precios',descripcion='Permite el Uso de uno solo o múltiple precios',
            observacion='1 - Un Solo Precio. 2 - Dos Precios. 3 - Tres Precios. n - etc.')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion6.id))

        cls.configuracion7, created = Configuracion.objects.get_or_create(
            nombre='Moneda',descripcion='Permite el uso de uno o dos monedas',
            observacion='0 - Soles. 1 - Dólares. 3. Ambos')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion7.id))

        cls.configuracion8, created = Configuracion.objects.get_or_create(
            nombre='Dias máximos dee anulación',descripcion='Cantidad de días máximos que puede pasar  después de la emisión de un comprobante',
            observacion='Número entre 1 y 7 es la cantidad de días')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion8.id))

        cls.configuracion9, created = Configuracion.objects.get_or_create(
            nombre='Ocultar Columna Placa',descripcion='Permite la visualizacion de la columna Placa por producto',
            observacion='0 - Oculta. 1 - Muestra')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion9.id))

        cls.configuracion10, created = Configuracion.objects.get_or_create(
            nombre='Ose / Sunat',descripcion='Verifica si los xml se enviarán a la OSE o SUNAT',
            observacion='0 - OSE. 1 - SUNAT')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion10.id))

        cls.configuracion11, created = Configuracion.objects.get_or_create(
            nombre='Direccion Envíos XML facturas/Boletas',descripcion='Registra la dirección que se usará para el envío de los XML de las Boletas y/o facturas')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion11.id))

        cls.configuracion12, created = Configuracion.objects.get_or_create(
            nombre='Dirección Envíos XML Notas de Crédito/débito',descripcion='Registra la dirección que se usará para el envió de los xml de las Notas de Crédito/Débito')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion12.id))

        cls.configuracion13, created = Configuracion.objects.get_or_create(
            nombre='Dirección Envíos XML Guías de Remisión',descripcion='Registra la dirección que se usará para el envió de los xml de las Guías de Remisión')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion13.id))

        cls.configuracion14, created = Configuracion.objects.get_or_create(
            nombre='Dirección Envíos XML para percepción y retención',descripcion='')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion14.id))

        cls.configuracion15, created = Configuracion.objects.get_or_create(
            nombre='Dirección de Anulación de Facturas',descripcion='')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion15.id))
        
        cls.configuracion16, created = Configuracion.objects.get_or_create(
            nombre='Dirección de Anulación de Notas de Crédito/Débito',descripcion='')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion16.id))

        cls.configuracion17, created = Configuracion.objects.get_or_create(
            nombre='Dirección de Anulación de Guías de Remisión',descripcion='')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion17.id))
        
        cls.configuracion18, created = Configuracion.objects.get_or_create(
            nombre='Dirección para consultas XML 1',descripcion='')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion18.id))

        cls.configuracion19, created = Configuracion.objects.get_or_create(
            nombre='Dirección para consultas XML 2',descripcion='')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion19.id))

        cls.configuracion20, created = Configuracion.objects.get_or_create(
            nombre='Dirección para consultas XML 3',descripcion='')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion20.id))

        cls.configuracion21, created = Configuracion.objects.get_or_create(
            nombre='Dirección para consultas XML 4',descripcion='')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion21.id))

        cls.configuracion22, created = Configuracion.objects.get_or_create(
            nombre='Ubicación base de datos',descripcion='Indica donde está el servidor de la base de datos',
            observacion='0 - local. 1 - Web-Cliente. 2 - Web-PeruFact')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion22.id))

        cls.configuracion23, created = Configuracion.objects.get_or_create(
            nombre='Cantidad máxima de Boletas por resumen',descripcion='',
            observacion='')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion23.id))
        
        cls.configuracion24, created = Configuracion.objects.get_or_create(
            nombre='Envío de XML Boletaspor resumen o individual',descripcion='',
            observacion='0 - Individual. 1 - Resumen')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion24.id))

        cls.configuracion25, created = Configuracion.objects.get_or_create(
            nombre='Fecha Inicio de Contraro',descripcion='',
            observacion='')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion22.id))

        cls.configuracion26, created = Configuracion.objects.get_or_create(
            nombre='Fecha de Renovación',descripcion='',
            observacion='')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion26.id))

        cls.configuracion27, created = Configuracion.objects.get_or_create(
            nombre='Activa o Desactiva el uso de productos de reemplazo',descripcion='',
            observacion='0 - Descativado. 1 - Activado')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion27.id))

        cls.configuracion28, created = Configuracion.objects.get_or_create(
            nombre='Mostrar Código de fabricante',descripcion='Permite Visualizar el código de fabricante en la búsqueda de productos',
            observacion='0 - Oculto. 1 - Visible')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion28.id))

        cls.configuracion29, created = Configuracion.objects.get_or_create(
            nombre='Mostrar Código de Proveedor',descripcion='',
            observacion='0 - Oculto. 1 - Visible')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion29.id))

        cls.configuracion30, created = Configuracion.objects.get_or_create(
            nombre='Mostrar Código Interno',descripcion='',
            observacion='0 - Oculto. 1 - Visible')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion30.id))

        cls.configuracion31, created = Configuracion.objects.get_or_create(
            nombre='Mostrar Código Sunat',descripcion='',
            observacion='0 - Oculto. 1 - Visible')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion31.id))

        cls.configuracion32, created = Configuracion.objects.get_or_create(
            nombre='Mostrar Código de Barras',descripcion='',
            observacion='0 - Oculto. 1 - Visible')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion32.id))

        cls.configuracion33, created = Configuracion.objects.get_or_create(
            nombre='Mostrar la presentación del Producto',descripcion='En Caso que tenga productos solo con presentaciones únicas se debe ocultar esta información',
            observacion='0 - Oculto. 1 - Visible')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion33.id))

        cls.configuracion34, created = Configuracion.objects.get_or_create(
            nombre='Ubicaciónde Exonerado',descripcion='Si la Empresa está ubicado en un lugar exonerado del IGV',
            observacion='0 - Exonerado. 1 - No Exonerado')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion34.id))

        cls.configuracion35, created = Configuracion.objects.get_or_create(
            nombre='Precio de Venta Independente por Caja',descripcion='Establece si los precios de venta serán independentes por caja o por sucursal',
            observacion='0 - Por Sucursal. 1 - Por Caja')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion35.id))

        cls.configuracion36, created = Configuracion.objects.get_or_create(
            nombre='Vales de salida de Efectivo',descripcion='Permite la creación de Vales de salida de efectivo',
            observacion='0 - No Permite. 1 - Permite')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion36.id))

        cls.configuracion37, created = Configuracion.objects.get_or_create(
            nombre='Vales de Salida de Cualquier producto para canje con factura',descripcion='',
            observacion='0 - No Permite. 1 - Permite')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion37.id))

        cls.configuracion38, created = Configuracion.objects.get_or_create(
            nombre='Vales de Salida de Cualquier producto para canje sin factura',descripcion='',
            observacion='0 - No Permite. 1 - Permite')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion38.id))

        cls.configuracion39, created = Configuracion.objects.get_or_create(
            nombre='Vales de Salida de Producto exclusivo para Vale',descripcion='',
            observacion='0 - No Permite. 1 - Permite')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion39.id))

        cls.configuracion40, created = Configuracion.objects.get_or_create(
            nombre='Cotizaciones',descripcion='',
            observacion='0 - No Permite. 1 - Permite')
        print(f'\nConfiguracion Creada con ID: '+str(cls.configuracion40.id))


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0006_auto_20210110_1057'),
    ]

    operations = [
         migrations.RunPython(ConfiguracionesDatos.cargar_datos)
    ]