let botonEnviar = document.getElementById("botonEnviar");
let botonEliminar = document.getElementById("botonEliminar");
let docentesFrom =document.getElementById("docentesFrom");
let docentesEnd = document.getElementById("docentesEnd")
let object_select = document.getElementById("controldocente")
let b = 0;
object_select.addEventListener('click',()=>{
    if(b===0){
        var content = object_select.parentNode.nextElementSibling;
        content.style.maxHeight = content.scrollHeight + "px";
        b=1;
    }else{
        var content = object_select.parentNode.nextElementSibling;
        content.style.maxHeight = null;
        b=0;
    }
   
})



function agregar(){
    let docente = document.createElement("option")
    let docentes = Array.from(docentesEnd.options)
    let bandera= 0;
    docente.setAttribute("value",docentesFrom.value)
    let docenteTexto = document.createTextNode(docentesFrom.value);
    docente.appendChild(docenteTexto);

    console.log(docentes)
    if(docentes.length==0){
        docentesEnd.add(docente);
    }else {
        for( let i=0; i<docentes.length; i++){
            if(docentes[i].value == docente.value){
                console.log("repetido")
                bandera=1;
            } 
        }
        if(bandera===0){
            docentesEnd.add(docente);
            bandera=0
        }
    }
}

function eliminar(){
    let opciones = Array.from(docentesEnd.selectedOptions)
    for(opcion of opciones){
        docentesEnd.remove(opcion.index);
        docentesFrom.add(opcion);
    }
}

botonEnviar.addEventListener('click',agregar);
botonEliminar.addEventListener('click',eliminar);
