var num = document.querySelector('input#n1')
var tab = document.querySelector('select#tab')
var res = document.querySelector('div#res')
var valores = []
var ent = document.addEventListener('keypress', function(e){
    if(e.key === 'Enter') {
        var btn = document.querySelector('input#but');
        btn.click(); 
    }
})

function isNumero(n) {
    if (Number(n) >= 1 && Number(n) <= 100) {
        return true
    } else {
        return false
    }
}
function inLista(n, l){
    if(l.indexOf(Number(n)) != -1) {
        return true
    } else {
        return false
    }
}


function adicionar() {
    if(isNumero(num.value) && !inLista(num.value, valores)) {
        valores.push(Number(num.value))
        var item = document.createElement('option')
        item.text = `Valor ${num.value} adicionado.`
        tab.appendChild(item)
        res.innerHTML = ''
    } else {
        alert('Digite um valor primeiro')
    } n1.value = ''
      n1.focus()
}
function finalizar() {
    let tot = valores.length
    let media = 0
    let soma = 0
    let menor = valores[0]
    let maior = valores[0]
    for(let pos in valores) {
        soma += valores[pos] 
        if (valores[pos] > maior)
        maior = valores[pos]
        if (valores[pos] < menor)
        menor = valores[pos]
    }
    media = soma / tot
    res.innerHTML = ''
    res.innerHTML += `<p>A lista em um total de ${tot}</p>`
    res.innerHTML += `<p>O maior numero da lista é o ${maior}</p>`
    res.innerHTML += `<p>O menor numero é o ${menor}</p>`
    res.innerHTML += `<p>A soma entre eles da ${soma}</p>`
    res.innerHTML += `<p>A media deles é ${media}</p>`
}
