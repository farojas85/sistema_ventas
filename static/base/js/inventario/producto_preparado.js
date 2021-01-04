var producto_primos = []

$(function(){
    MostrarProductosNoIngrediente()
    ObtenerProductoPrimos()
})

function MostrarProductosNoIngrediente()
{
    $.ajax({    
        url:  '/productos/lista-no-ingredientes',
        type:  'get',
        dataType:  'json',
        success: function  (datos) {
           
        }
    });
}

function ObtenerProductoPrimos()
{
    $.ajax({    
        url:  '/productos/lista-primos',
        type:  'get',
        dataType:  'json',
        success: function  (datos) {
            producto_primos = datos.productos
        }
    });
}

$('.btn-generar').on('click' ,function(){
    cantidad = $('#id_cantidad_ingredientes').val()
    objetos="";
    $('#ingredientes').html('')
    for(i=1;i<=cantidad;i++)
    {
        objetos += 
            "<div class='col-md-4' id='item_"+i+"'>"
                +"<div class='card card-sm card-success shadow-none border border-success'>"
                    +"<div class='card-header'>"
                        +"<h5 class=card-title'>Componente "+i+"</h4>"
                    +"</div>"
                    +"<div class='card-body'>"
                        +"<div class='row'>"
                            +"<div class='col-md-11'>"
                                +"<select class='form-control form-control-sm' id='producto_"+i+"'>"
                                +"</select>"
                            +"</div>"
                            +"<div class='col-md-1'>"
                                +"<button type='button' class='btn btn-sm btn-info btn'>"
                                +"</button>"
                            +"</div>"
                        +"</div>"
                    +"</div>"
                +"</div>"
            +"</div>"
    }

    
    $('#ingredientes').html(objetos)

   
    for(i=1;i<=cantidad;i++)
    {
        $('#producto_'+i).empty();
        $('#producto_'+i).append("<option value=''>-Seleccionar-</option>")

        producto_primos.forEach(prod => {
            $('#producto_'+i).append(`<option value=${prod.id}>${prod.nombre}</option>`)
        });
    }
})