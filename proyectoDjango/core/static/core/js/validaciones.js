
$("#nombre_vacio")[0].style.display="none";
$("#nombre_muy_largo")[0].style.display="none";
$("#nombre_invalido")[0].style.display = "none";

$("#apellidoP_vacio")[0].style.display="none";
$("#apellidoP_muy_largo")[0].style.display="none";
$("#apellidoP_invalido")[0].style.display = "none";

$("#apellidoM_vacio")[0].style.display="none";
$("#apellidoM_muy_largo")[0].style.display="none";
$("#apellidoM_invalido")[0].style.display = "none";

$("#correo_invalido")[0].style.display="none";
$("#correo_vacio")[0].style.display="none";

$("#comentarios_muy_largos")[0].style.display = "none";
$("#comentarios_vacio")[0].style.display = "none";
    

function validarNombre(){
    let nombre = $("#nombre")[0].value;
    $("#nombre_invalido")[0].style.display = "none";
    $("#nombre_vacio")[0].style.display = "none";
    $("#nombre_muy_largo")[0].style.display = "none";
    $("#nombre")[0].classList.remove("is-invalid");
    $("#nombre")[0].classList.add("is-valid");
    let rgNombre = /^[a-zA-Z]+$/;
    if (nombre.trim().length == 0){
        $("#nombre_invalido")[0].style.display = "none";
        $("#nombre_vacio")[0].style.display = "inline";
        $("#nombre_muy_largo")[0].style.display = "none";
        $("#nombre")[0].classList.add("is-invalid");
        return false;
    }
    if (rgNombre.test(nombre) == false){
        $("#nombre_invalido")[0].style.display = "inline";
        $("#nombre_vacio")[0].style.display = "none";
        $("#nombre_muy_largo")[0].style.display = "none";
        $("#nombre")[0].classList.add("is-invalid");
        return false;
    }
    if(nombre.trim().length > 30){
        $("#nombre_invalido")[0].style.display = "none";
        $("#nombre_vacio")[0].style.display = "none";
        $("#nombre_muy_largo")[0].style.display = "inline";
        
        $("#nombre")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

function validarApellidoP(){
    let apellido = $("#appaterno")[0].value;
    $("#apellidoP_invalido")[0].style.display = "none";
    $("#apellidoP_vacio")[0].style.display = "none";
    $("#apellidoP_muy_largo")[0].style.display = "none";
    $("#appaterno")[0].classList.remove("is-invalid");
    $("#appaterno")[0].classList.add("is-valid");
    let rgApellido = /^[a-zA-Z]+$/;
    if (apellido.trim().length == 0){
        $("#apellidoP_invalido")[0].style.display = "none";
        $("#apellidoP_vacio")[0].style.display = "inline";
        $("#apellidoP_muy_largo")[0].style.display = "none";
        $("#appaterno")[0].classList.add("is-invalid");
        return false;
    }
    if (rgApellido.test(apellido) == false){
        $("#apellidoP_invalido")[0].style.display = "inline";
        $("#apellidoP_vacio")[0].style.display = "none";
        $("#apellidoP_muy_largo")[0].style.display = "none";
        $("#appaterno")[0].classList.add("is-invalid");
        return false;
    }
    if(apellido.trim().length > 30){
        $("#apellidoP_invalido")[0].style.display = "none";
        $("#apellidoP_muy_largo")[0].style.display = "inline";
        $("#apellidoP_vacio")[0].style.display = "none";
        $("#appaterno")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

function validarApellidoM(){
    let apellido = $("#apmaterno")[0].value;
    $("#apellidoP_invalido")[0].style.display = "none";
    $("#apellidoM_vacio")[0].style.display = "none";
    $("#apellidoM_muy_largo")[0].style.display = "none";
    $("#apmaterno")[0].classList.remove("is-invalid");
    $("#apmaterno")[0].classList.add("is-valid");
    let rgApellido = /^[a-zA-Z]+$/;
    if (apellido.trim().length == 0){
        $("#apellidoP_invalido")[0].style.display = "none";
        $("#apellidoM_vacio")[0].style.display = "inline";
        $("#apellidoM_muy_largo")[0].style.display = "none";
        $("#apmaterno")[0].classList.add("is-invalid");
        return false;
    }
    if (rgApellido.test(apellido) == false){
        $("#apellidoP_invalido")[0].style.display = "inline";
        $("#apellidoM_vacio")[0].style.display = "none";
        $("#apellidoM_muy_largo")[0].style.display = "none";
        $("#apmaterno")[0].classList.add("is-invalid");
        return false;
    }
    if(apellido.trim().length > 30){
        $("#apellidoP_invalido")[0].style.display = "none";
        $("#apellidoM_muy_largo")[0].style.display = "inline";
        $("#apellidoM_vacio")[0].style.display = "none";
        $("#apmaterno")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

function validarCorreo(){
    let correo = $("#correo")[0].value;
    $("#correo_invalido")[0].style.display = "none";
    $("#correo_vacio")[0].style.display = "none";
    $("#correo")[0].classList.remove("is-invalid");
    $("#correo")[0].classList.add("is-valid");
    let rgEmail = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
    if (correo.trim().length == 0){
        $("#correo_invalido")[0].style.display = "none";
        $("#correo_vacio")[0].style.display = "inline";
        $("#correo")[0].classList.add("is-invalid");
        return false;
    }
    if (rgEmail.test(correo) == false){  
        $("#correo_vacio")[0].style.display = "none";
        $("#correo_invalido")[0].style.display = "inline";
        $("#correo")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

function validarComentarios(){
    let comentarios = $("#comentarios")[0].value;
    $("#comentarios_muy_largos")[0].style.display = "none";
    $("#comentarios_vacio")[0].style.display = "none";
    $("#comentarios")[0].classList.remove("is-invalid");
    $("#comentarios")[0].classList.add("is-valid");
    if(comentarios.trim().length > 100){
        $("#comentarios_muy_largos")[0].style.display = "inline";
        $("#comentarios_vacio")[0].style.display = "none";
        $("#comentarios")[0].classList.add("is-invalid");
        return false;
    }
    if(comentarios.trim().length == 0){
        $("#comentarios_muy_largos")[0].style.display = "none";
        $("#comentarios_vacio")[0].style.display = "inline";
        $("#comentarios")[0].classList.add("is-invalid");
        return false;
    }
    return true;
}

function validarInfoContacto(){
    if(!validarNombre()) return;
    if(!validarApellidoP()) return;
    if(!validarApellidoM()) return;
    if(!validarCorreo()) return;
    if(!validarComentarios()) return;
    document.getElementById("infocontacto").submit();
}
