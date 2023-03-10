function Validar() {

    //Coger los datos del formulario 
    var usuario = document.getElementById("usuario").value;
    var clave = document.getElementById("clave").value;

    if (usuario == "admin" && clave == "1234") {

        //Si somos administrador nos vamos a una web administrador
        window.location.pathname = '/administrador.html';



    } else {
        //Si algun dato está erroneo mostramos un mensaje
        document.getElementById("error").innerHTML="Datos del usuario erroneo";
    }

    if (usuario == "jose" && clave == "joseyale") {

        //Si somos usuario nos vamos a una web administrador
        window.location.pathname = '/Cristian.html';

    } else {
        //Si algun dato está erroneo mostramos un mensaje
        document.getElementById("error").innerHTML="Datos del usuario erroneo";

    }
}



function validacion(){

    var falta = document.getElementById("alta");

    //Campo nombre


    //campo edad

    var edad = falta.edad.value;
    if(edad == ""){
        alert("Escribe tu Edad")
        falta.edad.focus()
    }else if (isNaN(edad)){
        alert("Escribe un numero relacionado con tu edad");
        falta.edad.focus();
    }else if (edad <18){
        alert("Eres menor de Edad debes ser mayor de edad para poder registrate en nuestra plataforma")
        falta.edad.focus();
    }


    //campo ciudad

    if (falta.cuidad.selectedIndex == 0){
        alert("Elije una ciudad")
        falta.ciudad.focus();
    }

    alert("Muchaas gracias por Registrate");
    falta.submit();



    
    

}
