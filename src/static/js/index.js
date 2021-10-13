let object_select = document.getElementById("tipoCuenta")
object_select.addEventListener('change',()=>{
    if(object_select.value==='docente'){
        var content = object_select.parentNode.nextElementSibling;

            content.style.maxHeight = content.scrollHeight + "px";
        
    }else{
        var content = object_select.parentNode.nextElementSibling;
        content.style.maxHeight = null;
    }
   
})