// let min = document.getElementById('min')
// let max = document.getElementById('max')
//let boton= document.getElementById("guardar")
let formulario = document.getElementById('formulario')
const valcampmin = (e)=>{
    let min = formulario.cantMinimaAlum.value
    let max = formulario.cantMaximaAlum.value
    console.log('hola si entree bro')
    if(min > max){
        alert('min mayor que max ta mal bro')
        e.preventDefault()
    }
}
const valnull = () => {

} 
const validar = (e)=>{
    valcampmin(e);
}
    



formulario.addEventListener('submit',validar)