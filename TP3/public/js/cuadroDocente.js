let botonEnviar = document.getElementById("botonEnviar");
let botonEliminar = document.getElementById("botonEliminar");
let docentesFrom =document.getElementById("docentesFrom");
let docentesEnd = document.getElementById("docentesEnd")
function agregar(){
    let opciones= Array.from(docentesFrom.selectedOptions)
    for(opcion of opciones){
        docentesFrom.remove(opcion.index);
        docentesEnd.add(opcion);
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
