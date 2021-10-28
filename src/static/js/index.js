let object_select = document.getElementById("tipoCuenta")
let campoestudiante = document.getElementById("estudiante")
object_select.addEventListener('change',()=>{
    
    if(object_select.value==='docente'){
        campoestudiante.style.display="none"
        var content = object_select.parentNode.nextElementSibling;
        content.style.maxHeight = content.scrollHeight + "px";
        
    }else{
        campoestudiante.style.display="block"
        var content = object_select.parentNode.nextElementSibling;
        content.style.maxHeight = null;
    }
   
})