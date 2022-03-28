    var numb = document.querySelector('input#num1')
    var tab = document.querySelector('select#seltab')
    var res = document.querySelector('div#res')
    var array = []

function isNumero(n) {
 if(Number(n) >= 1 && Number(n) <= 100) {
     return true
 } else {
     return false
 }
}
    function inLista(n, l) {
if(l.indexOf(Number(n))!= -1) { // indexOf procura o elemento e da a casa onde ele esta
    return true
} else {
    return false
}
}

    
function verify() {
    if(isNumero(numb.value) && !inLista(numb.value, array)) { // ! significa NAO em js
     array.push(Number(numb.value))
     let item = document.createElement('option')
     item.text = `Valor ${numb.value} adicionado.`
     tab.appendChild(item)
     res.innerHTML = ''
    } else {
        alert('Valor invalido ou já encontrado na lista.')
    }
    num1.value = ''
    num1.focus() // esse comando serve para limpar a caixa apos o click, use com o codigo da linha de cima
}
function finalizar() {
    if (array.length == 0) {
        alert('Adicione valores antes de finalizar')
    } else {
        let tot = array.length
        let maior = array[0]
        let menor = array[0]
        let soma = 0
        let media = 0
        for(let pos in array) { // esse comando le o array por inteiro
            soma += array[pos]
            if (array[pos] > maior)
            maior = array[pos]
            if (array[pos] < menor)
            menor = array[pos]
        } 
        media = soma / tot
        res.innerHTML = ''
        res.innerHTML += `<p>Ao todo, temos ${tot} números cadastrados.</p>`
        res.innerHTML += `<p>O maior numero é o ${maior}.</p>`
        res.innerHTML += `<p>O menor numero é o ${menor}.</p>`
        res.innerHTML += `<p>Somando todos o valores temos ${soma}</p>`
        res.innerHTML += `<p>A media dos valores é ${media}</p>`
    }
}