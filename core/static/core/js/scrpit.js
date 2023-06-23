$(document).ready(function(){
    // ocultar la zona de mensajes de errores
    $('#errores').hide();

    // le agregamos que cuando haga click sobre submit
    $('#formulario').submit(function(){
        // capturar la info
        var nombre = $('#nom').val();
        var correo = $('#correo').val();
        var mensaje = '';
        if(correo == '') mensaje += '<h6>Debe ingresar Correo</h6>';
        if(nombre == '') mensaje += '<h6>Debe ingresar Contraseña</h6>';
        
        
        if(mensaje != ''){
            // traspasar el mensaje al #errores
            $('#errores').html(mensaje);
            $('#errores').show();
            // detener el submit
            event.preventDefault();
        }
    });
    // añade evento al boton reset
    $("#reset").click(function(){
        $('#errores').hide();
    });
});

$(document).ready(function(){
    // ocultar la zona de mensajes de errores
    $('#errores').hide();

    // le agregamos que cuando haga click sobre submit
    $('#formularioRegistro').submit(function(){
        // capturar la info
        var nombre = $('#nom').val();
        var apellido = $('#ape').val();
        var rut = $('#rut').val();
        var correo = $('#correo').val();
        var contraseña = $('#con').val();
        var mensaje = '';

        if(nombre == '') mensaje += '<h6>Debe ingresar Nombre</h6>';
        if(apellido == '') mensaje += '<h6>Debe ingresar Apellido</h6>';
        if(rut == '') mensaje += '<h6>Debe ingresar su Rut</h6>';
        if(correo == '') mensaje += '<h6>Debe ingresar Correo</h6>';
        if(contraseña == '') mensaje += '<h6>Debe ingresar Contraseña</h6>';
        
        
        
        if(mensaje != ''){
            // traspasar el mensaje al #errores
            $('#errores').html(mensaje);
            $('#errores').show();
            // detener el submit
            event.preventDefault();
        }
    });
    // añade evento al boton reset
    $("#reset").click(function(){
        $('#errores').hide();
    });
});