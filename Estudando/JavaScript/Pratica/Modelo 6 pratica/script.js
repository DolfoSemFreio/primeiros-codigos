function verify() {
    var ini = document.querySelector('input#num1')
    var fim = document.querySelector('input#num2')
    var pas = document.querySelector('input#num3')
    var res = document.querySelector('div#res')
    
    res.innerHTML = 'Inicio da contagem: '
    if (ini.value.length == 0 || fim.value.length == 0 || pas.value.length == 0) {
        alert('[ERRO] Por Favor preencha os campos')
     }          else {
                    var i = Number(ini.value)
                    var f = Number(fim.value)
                    var p = Number(pas.value)
            
            }           if (p <= 0) {
                            p = 1
            }
                            if (i < f) {

                                for (var j = i; j <= f; j += p) {
                                    res.innerHTML += `${j} `   
            } 
        }                               else if (f < i) {
                                            for (var j = i; j >= f; j-=p){
                                            res.innerHTML += `${j} `  
            }     
        } res.innerHTML += `; Fim da contagem<br> <strong>Volte Sempre</strong> `
 
}
