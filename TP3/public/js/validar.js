// let min = document.getElementById('min')
// let max = document.getElementById('max')
// let boton= document.getElementById("guardar")
let formulario = document.getElementById('formulario')
const valcampmin = (e)=>{
    let min = Number(formulario.cantMinimaAlum.value)
    let max = Number(formulario.cantMaximaAlum.value)
    if(min > max){
        alert('El número minimo de alumnos no puede ser superior al maximo de alumnos')
        e.preventDefault()
    }
}
const validarFecha = (e) => {
        fechainicio= new Date(formulario.fechaInicio.value)
        fechafinal= new Date(formulario.fechaFin.value)
        if(fechainicio>fechafinal){
            alert('La fecha de inicio de curso no debe ser posterior a la fecha de finalizacion del mismo')
            e.preventDefault()
        }
} 
const validar = (e)=>{
    valcampmin(e);
    validarFecha(e);
}
    



formulario.addEventListener('submit',validar)