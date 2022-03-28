var select = document.getElementById("marcas");

var opcaoTexto = select.options[select.selectedIndex].text;
var opcaoValor = select.options[select.selectedIndex].value;

console.log(opcaoTexto); // Ferrari
console.log(opcaoValor); // ferrari