function verify() {
    var ini = document.querySelector('input#numero1')
    var fi = document.querySelector('input#numero2')
    var pas = document.querySelector('input#passo')
    var res = document.querySelector('div#res')

    if (ini.value.length == 0 || fi.value.length == 0 || pas.value.length == 0) {
        res.innerHTML = ('[ERRO]Preencha os campos!')
    } else {
       //  res.innerHTML += ('Contando')
        var i = Number(ini.value)
        var f = Number(fi.value)
        var p = Number(pas.value)

        if (p <= 0) {
            p = 1
        }
            
        
        if (i < f) { //crescente
        for (var c = i; c <= f; c += p) {
      
     res.innerHTML += `${c} ` }

    } else {
        for (var c = i; c >= f; c -= p) {
            res.innerHTML += `${c} `
        } 
        
    }
    






        } 
    } 

