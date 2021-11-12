document.onreadystatechange = function(){
    if(document.readyState === 'complete'){
        let nota1=document.getElementById('id_nota1')
        let nota2=document.getElementById('id_nota2')
        let nota3=document.getElementById('id_nota3')
        let asistencia=document.getElementById('id_asistencia')
        
        nota1.hidden = true
        nota2.hidden = true
        nota3.hidden = true
        asistencia.hidden = true
        console.log(nota1)
    }
}