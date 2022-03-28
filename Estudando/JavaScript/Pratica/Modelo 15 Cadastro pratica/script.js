
var numero= document.querySelector('input#n1')
var tab = document.querySelector('select#tab')
var res = document.querySelector('div#result')
var arrays = []
var btn = document.addEventListener('keypress', function(e){
    if(e.key === 'Enter') {
        var btn = document.querySelector('input#but')
        btn.click()
    }
})
var clk = document.addEventListener('click', function(e){
    if(e.key === 'Click') {
        var clk = document.querySelector('select#tab')
        clk.click()
    }
})

function inNumero(n) {
    if (Number(n) >= 1) {
        return true
    } else {
        return false
    }

}

function inLista(n,l){
 if(l.indexOf(Number(n)) != -1) {
     return true
 } else {
     return false
 }
}

function Adicionar() {
    if(inNumero(numero.value) && !inLista(numero.value, arrays)) {
        arrays.pus(Number(numero.value))
        var item = document.createElement('option')
        item.id = `numbs ${numero.value}` 
        item.text = `${numero.value}`
        tab.appendChild(item) 
    } else {
        if ( numero.value.length === 0){
            alert('Por favor insira um numero')
        } else {
            alert('Numero ja se encontra na lista')
        }
    }
n1.value = ''
n1.focus()
} 
function opt(){
    var sele =  tab.value
    var  m2 = document.querySelector('div#result')
    m2.text = `${sele.value}`
    
    
}
 



