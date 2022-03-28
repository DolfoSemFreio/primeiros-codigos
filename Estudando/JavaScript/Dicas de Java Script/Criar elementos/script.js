function verify() {
    let num = document.querySelector(`input#num1`)
    let tab = document.querySelector(`select#seltab`)
    if (num.value.length ==0) { 
     alert(`[ERRO]Digite um numero`)
    } else {
       let n = Number(num.value)
       let c = 1 // let só pode ser usado dentro do bloco que foi criado
       tab.innerHTML = ''  // fazer isso pra aparecer só um resultado por vez 
       while (c <= 10) {
           let item = document.createElement(`option`) //Em um documento HTML, o método Document.createElement() cria o elemento HTML especificado ou um HTMLUnknownElement (en-US) se o nome do elemento dado não for conhecido, Este código cria uma nova <div> e a insere antes do elemento com ID "div1".
           item.text = `${n} x ${c} = ${n*c}`
           item.value = `tab${c}`
           tab.appendChild(item) // appendChild serve para criar  um novo elemento
           c++
       }
    }

}