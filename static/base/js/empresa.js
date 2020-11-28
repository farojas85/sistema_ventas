$.ajax({
    url:  '/departamento/list',
    type:  'get',
    dataType:  'json',
    success: function  (data) {
        $('#id_departamento').empty();
        $('#id_departamento').append("<option value=''>-Seleccionar-</option>")
        data.departamentos.forEach(depa => {
            $('#id_departamento').append(`<option value=${depa.id}>${depa.nombre}</option>`)
        });
    }
});

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