function verify() {
var ini = document.querySelector('input#inicio')
var fi = document.querySelector('input#fim')
var d = document.querySelector('input#passo')
var res = document.querySelector("div#res")

if (ini.value.length == 0 || fi.value.length == 0 || d.value.length == 0) { // esse x.value.length == 0 significar q esta tudo vazio
   res.innerHTML = `Impossivel contar.`
} else {
   res.innerHTML = 'Contando:<br>' // br e break lin, para pular a linha e tipo um paragrafo
   var i = Number(ini.value) // sempre q trabalhar com numero converter o querySelector fazendo outro var com um Number
   var f = Number(fi.value)
   var p = Number(d.value)
   if (p <= 0) {  // serve para contar o 0 como 1
      p = 1 
   }
   
   if (i < f) { // crescente 
   for (var c = i; c <= f; c += p) { // sempre criar um var novo dentro do for, e sempre verificar se usou o simbolo certo
      res.innerHTML += ` ${c} \u{1F595}`}
   } else { // decrescente
      for (var c = i; c >=f; c -= p) {
         res.innerHTML += ` ${c} \u{1F595}`  // esse codigo no final e um emoji
                                             // unicode.org/emoji/charts/full-emoji-list.html site de emoji
      }
   }
   res.innerHTML += `. <strong>Brasil acima de tudo</strong>` 
}

}