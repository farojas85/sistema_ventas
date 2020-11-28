$(function(){
    $('#form-sucursal').trigger('reset')
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
 
    $('#tabla-sucursal').DataTable({
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

$('#id_ruc').on('keyup',function(){
    ruc = String($(this).val())
    if(ruc.length == 11)
    {
        $.ajax({    
            url:  '/empresa/filtro',
            type:  'get',
            dataType:  'json',
            data:{ ruc : ruc },
            success: function  (data) {
                if(data)
                {
                    data.empresa.forEach(empresa => {
                        $('#id_empresa').val(empresa.id)
                        $('#id_razon_social').val(empresa.razon_social)
                    });
                }
            }
        });
    }
})

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
function sucursalMostrar(id,crud)
{
    $.ajax({    
        url:  '/sucursal/mostrar',
        type:  'get',
        dataType:  'json',
        data:{ id : id },
        success: function  (datos) {
            let sucursali = datos.sucursal
            let empresa = datos.empresa
            let ubigeo = datos.ubigeo
            let provincia = datos.provincia
            let departamento = datos.departamento
            empresa.forEach(emp => {
                $('#id_empresa').val(emp.id)
                $('#id_ruc').val(emp.ruc)
                $('#id_razon_social').val(emp.razon_social)
            })
            sucursali.forEach(sucursal => {
                $('#id').val(sucursal.id)
                $('#id_nombre').val(sucursal.nombre)
                $('#id_direccion').val(sucursal.direccion)
                $('#id_referencia').val(sucursal.referencia)
                $('#id_observacion').val(sucursal.observacion)
                $('#id_estado').prop('checked',sucursal.estado)
            })
            listarDepartamentosMostrar(departamento[0].id)
            listarProvinciasMostar(departamento[0].id,provincia[0].id)
            listarDistritosMostrar(provincia[0].id,ubigeo[0].id)

            $('#modal-sucursal').modal('show')
        }
    });
}

$('.btn-mostrar').on('click',function(){
    let id= $(this).data('id')
    sucursalMostrar(id,'mostrar')
    $(".btn-guardar").css("display", "none")
})

$('.btn-editar').on('click',function(){
    let id= $(this).data('id')
    sucursalMostrar(id,'editar')
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