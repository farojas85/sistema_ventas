$(function(){
    listarEmpresas()
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