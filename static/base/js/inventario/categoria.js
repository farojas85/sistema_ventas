$(function(){
    $('#tabla-categoria').DataTable({
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
                },
                "sZeroRecords": "No hay Registros que mostrar",
                "sEmptyTable": "No hay Datos Disponibles"
            },
        "pageLength": 10,
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
        "order": [[ 0, "desc" ]]
    })
})

$('.btn-nuevo').on('click' ,function(){
    $.ajax({    
        url:  '/categoria/crear',
        type:  'get',
        dataType:'json',
        success: function  (datos) {
            $('#modal-default-title').html('Nueva Categoría')
            $('#modal-default').modal('show')
            $('#modal-default-body').html(datos.html_form)
            $('#id_estado').prop('checked', true);
            $('#estado_crud').val('crear')
            $('#modal-btn-guardar').css('display','')
        }
    });
})

$("#modal-default").on("submit", ".js-create-form", function (event) {
    event.preventDefault()
    var crud = $('#estado_crud').val()
    var form = $(this);
    var id = $("#categoria_id").val()

    switch(crud){
        case 'crear' : insertar(form);break;
        case 'editar': actualizar(form,id);break;
    }
    return false;
});

function insertar(form){
    $.ajax({
        url: '/categoria/crear',
        data: form.serialize(),
        type:  form.attr('method'),
        dataType: 'json',
        success: function (datos) {
            if (datos.form_is_valid) {
                $('#modal-default').modal('hide')
                Swal.fire({
                    icon: 'success',
                    title:'Categorías',
                    text: 'Categoría registrada Satisfactoriamente',
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Aceptar'
                }).then((resultado) => {
                    if(resultado.isConfirmed) {
                        window.location="/categoria"
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
        url:  '/categoria/'+id+'/actualizar',
        data: form.serialize(),
        type:  form.attr('method'),
        dataType: 'json',
        success: function (datos) {
            if (datos.form_is_valid) {
                $('#modal-default').modal('hide')
                Swal.fire({
                    icon: 'success',
                    title:'Categorías',
                    text: 'Categoría Modificada Satisfactoriamente',
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Aceptar'
                }).then((resultado) => {
                    if (resultado.isConfirmed) {
                        
                        window.location="/categoria"
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
        url:  '/categoria/'+id+'/actualizar',
        type:  'get',
        dataType:'json',
        success: function  (datos) {
            $('#modal-default-title').html('Editar Categoría')
            $('#modal-default').modal('show')
            $('#modal-default-body').html(datos.html_form)
            $('#id_estado').prop('checked', true);
            $('#categoria_id').val(id)
            $('#estado_crud').val('editar')
            $('#modal-btn-guardar').css('display','')
        }
    });   
})

$('.btn-eliminar').on('click' ,function(){
    let id= $(this).data('id')
    $('#id_categoria').val(id)
    $('#modal-categoria-eliminar').modal('show')   
})

$('.btn-inhabilitar').on('click',function(){
    form = $('#form-categoria-eliminar')
    $.ajax({    
        url:  '/categoria/inhabilitar',
        type:  'POST',
        data:form.serialize(),
        dataType: 'json',
        success: function  (datos) {
            if(datos.ok == 1)
            {
                $('#modal-categoria-eliminar').modal('hide')
                Swal.fire({
                    icon: 'success',
                    title:'Categorías',
                    text: 'Categoría Inhabilitada Satisfactoriamente',
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Aceptar'
                }).then((resultado) => {
                    if (resultado.isConfirmed) {
                        
                        window.location="/categoria"
                    }
                })
            }
        }
    });  
})

$('.btn-restaurar').on('click',function(){
    let id= $(this).data('id')
    $('#id_categoria_habilitar').val(id)
    $('#modal-categoria-restaurar').modal('show')   
})

$('.btn-habilitar').on('click',function(){
    form = $('#form-categoria-habilitar')
    $.ajax({    
        url:  '/categoria/habilitar',
        type:  'POST',
        data:form.serialize(),
        dataType: 'json',
        success: function  (datos) {
            if(datos.ok == 1)
            {
                $('#modal-categoria-restaurar').modal('hide') 
                Swal.fire({
                    icon: 'success',
                    title:'Categorías',
                    text: 'Categoría Habilitada Satisfactoriamente',
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Aceptar'
                }).then((resultado) => {
                    if (resultado.isConfirmed) {
                        window.location="/categoria"
                    }
                })
            }
        }
    });
})

$('.btn-eliminar-categoria').on('click' ,function(){
    form = $('#form-categoria-eliminar')
    $.ajax({    
        url:  '/categoria/eliminar',
        type:  'POST',
        data:form.serialize(),
        dataType: 'json',
        success: function(datos) {
            $('#modal-categoria-eliminar').modal('hide')
            if(datos.ok == 1)
            {
                Swal.fire({
                    icon: 'success',
                    title:'Categorías',
                    text: datos.mensaje,
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Aceptar'
                }).then((resultado) => {
                    if (resultado.isConfirmed)
                    {                        
                        window.location="/categoria"
                    }
                })
            } else {
                Swal.fire({
                    icon: 'warning',
                    title:'Categorías',
                    text: datos.mensaje,
                    confirmButtonColor: '#3085d6',
                    confirmButtonText: 'Aceptar'
                }).then((resultado) => {
                    if (resultado.isConfirmed) 
                    {                        
                        window.location="/categoria"
                    }
                })
            }
        }
    });  
})