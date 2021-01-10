$(function(){
    listarEmpresas()

    $('#tabla-producto').DataTable({
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

function listarEmpresas(){
    $.ajax({    
        url:  '/empresa/lista',
        type:  'get',
        dataType:  'json',
        success: function  (datos) {
            $('#id_empresa').empty();
            $('#id_empresa').append("<option value='' selected>-Seleccionar-</option>")
            datos.empresas.forEach(empresa => {
                $('#id_empresa').append(`<option value=${empresa.id}>${empresa.razon_social}</option>`)
            });
        }
    });
}

function listarCategorias() {
    
}