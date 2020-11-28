$(function(){
    $('#form-empresa').trigger('reset')
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
 
    $('#tabla-empresa').DataTable({
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