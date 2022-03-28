var numb = document.querySelector('input#num1')
var tab = document.querySelector('select#tab')
var res = document.querySelector('div#res')
var valores = []
var ent = document.addEventListener('keypress', function(e) { // esse comando serve para clicar usando o enter
    if(e.key === 'Enter') {
        var btn = document.querySelector('input#but');
        btn.click(); 
    }
})


function isNumero(n) {
    if(Number(n) >= 1 && Number(n) <= 100) {
        return true
    } else {
        return false
    }
}
function inLista(n, l){
    if (l.indexOf(Number(n))!= -1) {
        return true
    } else {
        return false
    }
}


function adicionar() {
    if(isNumero(numb.value) && !inLista(numb.value, valores)) {
        valores.push(Number(numb.value))
        let item = document.createElement('option')
        item.text = `Valor ${numb.value} adicionado`
        tab.appendChild(item)
        res.innerHTML = ''
    } else {
        alert('Valor invalido ou Ja encontrado na lista')
    }
    num1.value = ''
    num1.focus()
}

function finalizar(){
    if(valores.length == 0) {
        alert('Adicione valores para continuar')
    } else {
        let tot = valores.length
        let maior = valores[0]
        let menor = valores[0]
        let media = 0  
        let soma = 0
        for(let pos in valores){
            soma += valores[pos]
            if (valores[pos] > maior)
            maior = valores[pos]
            if (valores[pos] < menor)
            menor = valores[pos]
        }
        media = soma / tot
        res.innerHTML = ''
        res.innerHTML += `<p>A lista tem um total de ${tot} números.</p>`
        res.innerHTML += `<p>O maior numero da lista é o ${maior}.</p>`
        res.innerHTML += `<p>O menor numero da lista é ${menor}.</p>`
        res.innerHTML += `<p>A media entre eles é ${media}.</p>`
        res.innerHTML += `<p>A soma deles da ${soma}.</p>`
        res.innerHTML += `<p><strong>🔥Volte Sempre🔥.</strong></p>`
    }
    
}