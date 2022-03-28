var seltab = document.querySelector('input#tab')
var numb = document.querySelector('input#n1')
var res = document.querySelector('div#res')
var valores = []
var btn = document.addEventListener('keypress', function(e) {
    if(e.key === 'Enter') {
        var btn = document.querySelector('input#ad');
        btn.click();
    }
}
)
function fatorial(n) {
    if (n == 1) {
        return 1
    } else {
        return n * fatorial(n-1)
    }
}

function isNumero(n){
 if(Number(n) >= 1 && Number(n) <= 100) {
     return true
 } else {
     return false
 }
}
function inLista(n, l) {
    if(l.indexOf(Number(n)) != -1) {
        return true 
    } else {
        return false
    }
}
function adicionar() {
    if (isNumero(numb.value) && !inLista(numb.value, valores)) {
    valores.push(Number(numb.value))
    let item = document.createElement('option')
    item.text = `Valor ${numb.value} adicionado`
    tab.appendChild(item)
    res.innerHTML = ''
    } else {
        if (numb.value.length == 0) {
            alert('Primeiro digite um numero')
        } else {
            alert('O numero ja foi adicionado ou é invalido')
        }
    } 
    n1.value = ''
    n1.focus()
      
}
function finalizar() {
    tot = valores.length
    soma = 0
    media = 0
    maior = valores[0]
    menor = valores[0]
    for (let pos in valores) {
        soma += valores[pos]
        if (valores[pos] > maior)
            maior = valores[pos]
        if (valores[pos] < menor)
            menor = valores[pos]
    }
    media = soma / tot
    res.innerHTML = ''
    res.innerHTML += `<p>O total de números adicionado foi de ${tot}</p>`
    res.innerHTML += `<p>A soma entre eles da ${soma}</p>`
    res.innerHTML += `<p>O maior numero entre eles é ${maior}</p>`
    res.innerHTML += `<p>O menor numero entre eles é ${menor}</p>`
    res.innerHTML += `<p>A media deles é ${media}</p>`
    res.innerHTML += `<p>O fatorial do maior numero deles da ${fatorial(maior)}</p>`
    res.innerHTML += `<p>O fatorial do menor numero deles da ${fatorial(menor)}</p>`
    }

