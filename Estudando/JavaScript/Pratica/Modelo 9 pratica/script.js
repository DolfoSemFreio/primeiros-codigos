function verify() {
    let ini = document.querySelector('input#inicio')
    let fim = document.querySelector('input#fim')
    let passo = document.querySelector('input#passo')
    let res = document.querySelector('div#res')
    if (ini.value.length == 0 || fim.value.length ==0 || passo.value.length == 0) {
        alert('[ERRO]Por favor preencha os campos abaixo')
    } else {
        var i = Number(ini.value)
        var f = Number(fim.value)
        var p = Number(passo.value)
        res.innerHTML = ''
    
     if (i < f) {  // crescente  
         for (var c = i; c <= f; c += p) {
        res.innerHTML += ` ${c}`
}
    } else {
         for (var c = i;c >= f; c -= p) {
        res.innerHTML += ` ${c}`
    }
    }
    }
}