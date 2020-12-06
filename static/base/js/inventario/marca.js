$(function(){
    $('#tabla-marca').DataTable({
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
        "pageLength": 10,
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
    })
})
$('.btn-nuevo').on('click' ,function(){
    $.ajax({    
        url:  '/marca/crear',
        type:  'get',
        dataType:'json',
        success: function  (datos) {
            $('#modal-default-title').html('Nueva Marca')
            $('#modal-default').modal('show')
            $('#modal-default-body').html(datos.html_form)
            $('#id_estado').prop('checked', true);
            $('#estado_crud').val('crear')
            $('#modal-btn-guardar').css('display','')
        }
    });
})

$("#modal-default").on("submit", ".js-marca-create-form", function (event) {
    event.preventDefault()
    var crud = $('#estado_crud').val()
    var form = $(this);
    var id = $("#marca_id").val()
    console.log(form.serialize())
    switch(crud){
        case 'crear' : insertar(form);break;
        case 'editar': actualizar(form,id);break;
    }
    return false;
});

function insertar(form){
    $.ajax({
        url: '/marca/crear',
        data: form.serialize(),
        type:  form.attr('method'),
        dataType: 'json',
        success: function (datos) {
            if (datos.form_is_valid) {
                $('#modal-default').modal('hide')
                Swal.fire({
                    icon: 'success',
                    title:'Marcas',
                    text: 'Marca registrada Satisfactoriamente',
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Aceptar'
                }).then((resultado) => {
                    if(resultado.isConfirmed) {
                        window.location="/marca"
                    }
                })
            }
            else {
                $("#modal-default-body").html(datos.html_form);
            }
        }
    });
}
function actualizar(form,id) {
    $.ajax({
        url:  '/marca/'+id+'/actualizar',
        data: form.serialize(),
        type:  form.attr('method'),
        dataType: 'json',
        success: function (datos) {
            if (datos.form_is_valid) {
                $('#modal-default').modal('hide')
                Swal.fire({
                    icon: 'success',
                    title:'Marcas',
                    text: 'Marca Modificada Satisfactoriamente',
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Aceptar'
                }).then((resultado) => {
                    if (resultado.isConfirmed) {
                        
                        window.location="/marca"
                    }
                })
            }
            else {
                $("#modal-default-body").html(datos.html_form);
            }
        }
    });
}
$('.btn-editar').on('click' ,function(){
    let id= $(this).data('id')
    $.ajax({    
        url:  '/marca/'+id+'/actualizar',
        type:  'get',
        dataType:'json',
        success: function  (datos) {
            $('#modal-default-title').html('Nueva Marca')
            $('#modal-default').modal('show')
            $('#modal-default-body').html(datos.html_form)
            $('#id_estado').prop('checked', true);
            $('#marca_id').val(id)
            $('#estado_crud').val('editar')
            $('#modal-btn-guardar').css('display','')
        }
    });   
})

$('.btn-eliminar').on('click' ,function(){
    let id= $(this).data('id')
    $('#id_marca').val(id)
    $('#modal-marca-eliminar').modal('show')   
})

$('.btn-inhabilitar').on('click',function(){
    form = $('#form-marca-eliminar')
    $.ajax({    
        url:  '/marca/inhabilitar',
        type:  'POST',
        data:form.serialize(),
        dataType: 'json',
        success: function  (datos) {
            if(datos.ok == 1)
            {
                $('#modal-marca-eliminar').modal('hide')
                Swal.fire({
                    icon: 'success',
                    title:'Marcas',
                    text: 'Marca Inhabilitada Satisfactoriamente',
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Aceptar'
                }).then((resultado) => {
                    if (resultado.isConfirmed) {
                        
                        window.location="/marca"
                    }
                })
            }
        }
    });  
})

$('.btn-restaurar').on('click',function(){
    let id= $(this).data('id')
    $('#id_marca_habilitar').val(id)
    $('#modal-marca-restaurar').modal('show')   
}) 

$('.btn-habilitar').on('click',function(){
    form = $('#form-marca-habilitar')
    $.ajax({    
        url:  '/marca/habilitar',
        type:  'POST',
        data:form.serialize(),
        dataType: 'json',
        success: function  (datos) {
            if(datos.ok == 1)
            {
                $('#modal-marca-restaurar').modal('hide') 
                Swal.fire({
                    icon: 'success',
                    title:'Marcas',
                    text: 'Marca Habilitada Satisfactoriamente',
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Aceptar'
                }).then((resultado) => {
                    if (resultado.isConfirmed) {
                        
                        window.location="/marca"
                    }
                })
            }
        }
    });
})

$('.btn-eliminar-marca').on('click' ,function(){
    form = $('#form-marca-eliminar')
    $.ajax({    
        url:  '/marca/eliminar',
        type:  'POST',
        data:form.serialize(),
        dataType: 'json',
        success: function(datos) {
            $('#modal-marca-eliminar').modal('hide')
            if(datos.ok == 1)
            {
                Swal.fire({
                    icon: 'success',
                    title:'Marcas',
                    text: datos.mensaje,
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Aceptar'
                }).then((resultado) => {
                    if (resultado.isConfirmed)
                    {                        
                        window.location="/marca"
                    }
                })
            } else {
                Swal.fire({
                    icon: 'warning',
                    title:'Marcas',
                    text: datos.mensaje,
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Aceptar'
                }).then((resultado) => {
                    if (resultado.isConfirmed) 
                    {                        
                        window.location="/marca"
                    }
                })
            }
        }
    });  
})