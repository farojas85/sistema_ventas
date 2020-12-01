$(function(){
    $('#form-almacen').trigger('reset')
    $.ajax({
        url:  '/departamento/list',
        type:  'get',
        dataType:  'json',
        success: function  (data) {
            $('#id_departamento').empty();
            $('#id_departamento').append("<option value=''>-Seleccionar-</option>")
            data.departamentos.forEach(depa => {
                $('#id_departamento').append(`<option value=${depa.id}>${depa.nombre}</option>`)
            })
        }
    })

    $.ajax({
        url:  '/tipo-almacen/lista',
        type:  'get',
        dataType:  'json',
        success: function  (data) {
            $('#id_tipo_almacen').empty();
            $('#id_tipo_almacen').append("<option value=''>-Seleccionar-</option>")
            data.tipo_almacenes.forEach(depa => {
                $('#id_tipo_almacen').append(`<option value=${depa.id}>${depa.nombre}</option>`)
            })
        }
    })

    $.ajax({
        url:  '/unidad-medida/lista',
        type:  'get',
        dataType:  'json',
        success: function  (data) {
            $('#id_unidad_medidad').empty();
            $('#id_unidad_medidad').append("<option value=''>-Seleccionar-</option>")
            data.unidad_medidas.forEach(depa => {
                $('#id_unidad_medidad').append(`<option value=${depa.id}>${depa.nombre}</option>`)
            })
        }
    })
 
    $('#tabla-almacen').DataTable({
        "language":
            {
                "sProcessing":     "Procesando...",
                "sLengthMenu":     "Mostrar _MENU_ registros",
                "sZeroRecords":    "No se encontraron resultados",
                "sEmptyTable":     "Ningún dato disponible en esta tabla",
                "sInfo":           "Mostrando del _START_ al _END_ de un total de _TOTAL_",
                "sInfoEmpty":      "Mostrando del 0 al 0 de un total de 0",
                "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
                "sInfoPostFix":    "",
                "sSearch":         "Buscar:",
                "sUrl":            "",
                "sInfoThousands":  ",",
                "sLoadingRecords": "Cargando...",
                "oPaginate": {
                    "sFirst":    "Primero",
                    "sLast":     "Último",
                    "sNext":     "Siguiente",
                    "sPrevious": "Anterior"
                },
                "oAria": {
                    "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                    "sSortDescending": ": Activar para ordenar la columna de manera descendente"
                }
            },
        "pageLength": 5,
        "lengthMenu": [[5,10, 25, 50, -1], [5,10, 25, 50, "All"]],
    })
})

function listarProvincias()
{
    departamento =$("#id_departamento").val()
    $.ajax({    
        url:  '/provincia/list_by_departamento',
        type:  'get',
        dataType:  'json',
        data:{ departamento : departamento},
        success: function  (data) {
            $('#id_provincia').empty();
            $('#id_provincia').append("<option value=''>-Seleccionar-</option>")
            data.provincias.forEach(prov => {
                $('#id_provincia').append(`<option value=${prov.id}>${prov.nombre}</option>`)
            });
        }
    });
}

function listarDistritos()
{
    provincia =$("#id_provincia").val()
    $.ajax({    
        url:  '/distrito/list_by_provincia',
        type:  'get',
        dataType:  'json',
        data:{ provincia : provincia},
        success: function  (data) {
            $('#id_ubigeo').empty();
            $('#id_ubigeo').append("<option value=''>-Seleccionar-</option>")
            data.distritos.forEach(distrito => {
                $('#id_ubigeo').append(`<option value=${distrito.id}>${distrito.nombre}</option>`)
            });
        }
    });
}

$('.btn-buscar-sucursal').on('click',function(){
    $('#buscar_sucursal').val('')
    $('#tabla-buscar-sucursal').DataTable().destroy()
    $("#tabla-buscar-sucursal tbody tr").remove()
    $('#modal-buscar-sucursal').modal('show')
})

$('#buscar_sucursal').on('keyup',function(){
    let buscar = String($(this).val())
    $.ajax({    
        url:  '/sucursal/buscar',
        type:  'get',
        dataType:  'json',
        data:{ buscar : buscar },
        success: function  (data) {
            let sucursales = data.sucursales
            $('#tabla-buscar-sucursal').DataTable().destroy()
            $("#tabla-buscar-sucursal tbody tr").remove()
            if(sucursales.length == 0)
            {
                var html = '<tr>'+
                            '<td >'+
                            '</td>'+
                            '<td>--DATOS NO ENCONTRADOS--</td>'+
                            '</tr>'
                $("#tabla-buscar-sucursal tbody").append(html)
            }
            sucursales.forEach(suc => {
                var html = '<tr>'+
                            '<td >'+
                            '<button type="button" class="btn btn-success btn-xs btn-seleccionar-sucursal" onclick="seleccionarSucursal('+suc.id+')">'+
                            '<i class="fas fa-check"><i>'+
                            '</button>'+
                            '</td>'+
                            '<td>'+suc.nombre+'</td>'+
                            '</tr>'
                $("#tabla-buscar-sucursal tbody").append(html)
            })
           
            $('#tabla-buscar-sucursal').DataTable({
                "language":
                    {
                        "sProcessing":     "Procesando...",
                        "sLengthMenu":     "Mostrar _MENU_ registros",
                        "sZeroRecords":    "No se encontraron resultados",
                        "sEmptyTable":     "Ningún dato disponible en esta tabla",
                        "sInfo":           "Mostrando del _START_ al _END_ de un total de _TOTAL_",
                        "sInfoEmpty":      "Mostrando del 0 al 0 de un total de 0",
                        "sInfoFiltered":   "(filtrado de un total de _MAX_ registros)",
                        "sInfoPostFix":    "",
                        "sSearch":         "Buscar:",
                        "sUrl":            "",
                        "sInfoThousands":  ",",
                        "sLoadingRecords": "Cargando...",
                        "oPaginate": {
                            "sFirst":    "Primero",
                            "sLast":     "Último",
                            "sNext":     "Siguiente",
                            "sPrevious": "Anterior"
                        },
                        "oAria": {
                            "sSortAscending":  ": Activar para ordenar la columna de manera ascendente",
                            "sSortDescending": ": Activar para ordenar la columna de manera descendente"
                        }
                    },
                "pageLength": 5,
                "lengthMenu": [[5,10, 25, 50, -1], [5,10, 25, 50, "All"]],
            })
        }
    });
})

function seleccionarSucursal(id)
{
    $.ajax({    
        url:  '/sucursal/por-id',
        type:  'get',
        dataType:  'json',
        data:{ id : id},
        success: function  (data) {
            let sucursal =data.sucursal        
            sucursal.forEach(suc => {
                $('#id_sucursal').val(suc.id)
                $('#id_nombre_sucursal').val(suc.nombre)
            })
            $('#modal-buscar-sucursal').modal('hide')
        }
    });
}

function listarDepartamentosMostrar(departamento)
{
    $.ajax({
        url:  '/departamento/list',
        type:  'get',
        dataType:  'json',
        success: function  (data) {
            $('#id_departamento').empty();
            $('#id_departamento').append("<option value=''>-Seleccionar-</option>")
            data.departamentos.forEach(depa => {
                if(depa.id == departamento){
                    $('#id_departamento').append(`<option value=${depa.id} selected>${depa.nombre}</option>`)    
                } else {
                    $('#id_departamento').append(`<option value=${depa.id}>${depa.nombre}</option>`)
                }
            })
        }
    })
}

function listarProvinciasMostar(departamento,provincia)
{
    $.ajax({    
        url:  '/provincia/list_by_departamento',
        type:  'get',
        dataType:  'json',
        data:{ departamento : departamento},
        success: function  (data) {
            $('#id_provincia').empty();
            $('#id_provincia').append("<option value=''>-Seleccionar-</option>")
            data.provincias.forEach(prov => {
                if(prov.id == provincia){
                    $('#id_provincia').append(`<option value=${prov.id} selected>${prov.nombre}</option>`)    
                } else {
                    $('#id_provincia').append(`<option value=${prov.id}>${prov.nombre}</option>`)
                }
                
            });
        }
    });
}
function listarDistritosMostrar(provincia,distrito)
{
    $.ajax({    
        url:  '/distrito/list_by_provincia',
        type:  'get',
        dataType:  'json',
        data:{ provincia : provincia},
        success: function  (data) {
            $('#id_ubigeo').empty();
            $('#id_ubigeo').append("<option value=''>-Seleccionar-</option>")
            data.distritos.forEach(dist => {
                if(dist.id == distrito){
                    $('#id_ubigeo').append(`<option value=${dist.id} selected>${dist.nombre}</option>`)
                } else {
                    $('#id_ubigeo').append(`<option value=${dist.id}>${dist.nombre}</option>`)
                }
                
            });
        }
    });
}

function listarTipoAlmacenMostrar(tipo)
{
    $.ajax({    
        url:  '/tipo-almacen/lista',
        type:  'get',
        dataType:  'json',
        success: function  (data) {
            $('#id_tipo_almacen').empty();
            $('#id_tipo_almacen').append("<option value=''>-Seleccionar-</option>")
            data.tipo_almacenes.forEach(dist => {
                if(dist.id == tipo){
                    $('#id_tipo_almacen').append(`<option value=${dist.id} selected>${dist.nombre}</option>`)
                } else {
                    $('#id_tipo_almacen').append(`<option value=${dist.id}>${dist.nombre}</option>`)
                }
                
            });
        }
    });
}

function listarUnidadMedidaMostrar(tipo)
{
    $.ajax({    
        url:  '/unidad-medida/lista',
        type:  'get',
        dataType:  'json',
        success: function  (data) {
            $('#id_unidad_medida').empty();
            $('#id_unidad_medida').append("<option value=''>-Seleccionar-</option>")
            data.unidad_medidas.forEach(dist => {
                if(dist.id == tipo){
                    $('#id_unidad_medida').append(`<option value=${dist.id} selected>${dist.nombre}</option>`)
                } else {
                    $('#id_unidad_medida').append(`<option value=${dist.id}>${dist.nombre}</option>`)
                }
                
            });
        }
    });
}

function almacenMostrar(id,crud)
{
    $.ajax({    
        url:  '/almacen/mostrar',
        type:  'get',
        dataType:  'json',
        data:{ id : id },
        success: function  (datos) {
            let almacen = datos.almacen
            let sucursal = datos.sucursal
            let ubigeo = datos.ubigeo
            let provincia = datos.provincia
            let departamento = datos.departamento
            sucursal.forEach(emp => {
                $('#id_sucursal').val(emp.id)
                $('#id_nombre_sucursal').val(emp.nombre)
            })

            almacen.forEach(sucursal => {
                $('#id').val(sucursal.id)
                $('#id_nombre').val(sucursal.nombre)
                $('#id_direccion').val(sucursal.direccion)
                $('#id_area').val(sucursal.area)
                $('#id_capacidad').val(sucursal.capacidad)
                $('#id_unidad_medida').val(sucursal.unidad_medida)
                $('#id_estado').prop('checked',sucursal.estado)
            })
            listarTipoAlmacenMostrar(almacen[0].tipo_almacen_id)
            listarDepartamentosMostrar(departamento[0].id)
            listarProvinciasMostar(departamento[0].id,provincia[0].id)
            listarDistritosMostrar(provincia[0].id,ubigeo[0].id)
            listarUnidadMedidaMostrar(almacen[0].unidad_medidad_id)

            $('#modal-almacen').modal('show')
        }
    });
}

$('.btn-mostrar').on('click',function(){
    let id= $(this).data('id')
    almacenMostrar(id,'mostrar')
    $(".btn-guardar").css("display", "none")
})

$('.btn-editar').on('click',function(){
    let id= $(this).data('id')
    almacenMostrar(id,'editar')
    $(".btn-guardar").css("display", "block")
})

$('.btn-guardar').on('click' ,function(){
    form = $('#form-sucursal')
    $.ajax({
        url: '/sucursal/actualizar',
        type:  'post',
        dataType:  'json',
        data: form.serialize(),
        success: function(respuesta){
            if (respuesta.ok==1){
                Swal.fire({
                    icon: 'success',
                    title: 'Sucursal Modificado Satisfactoriamente',
                    showConfirmButton: false,
                    timer: 1000
                })
                $('modal-sucursal').modal('hide')
                window.location.href="/sucursal"
            }
        }
    });
})

$('.btn-eliminar').on('click' ,function(){
    let id= $(this).data('id')
    $('#id_sucursal').val(id)
    $('#modal-sucursal-eliminar').modal('show')   
})

$('.btn-eliminar-sucursal').on('click' ,function(){
    form = $('#form-sucursal-eliminar')
    console.log(form.serialize())
    $.ajax({
        url: '/sucursal/eliminar',
        type:  'post',
        dataType:  'json',
        data: form.serialize(),
        success: function(respuesta){
            if (respuesta.ok==1){
                Swal.fire({
                    title: 'Sucursal',
                    text: 'Registro de Sucursal eliminado Satisfactoriamente',
                    icon: 'success',
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Si',
                    cancelButtonText: 'No'
                }).then((result) => {
                    if (result.isConfirmed) {          
                        $('#modal-sucursal-eliminar').modal('hide')
                        window.location.href="/sucursal"
                    }
                })               
            }
        }
    })
})