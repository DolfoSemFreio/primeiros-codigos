var agora = new Date() // sempre date para pegar qualquer coisa envolvida com date e hora
var hora = agora.getHours() //var x.getX() é para pegar elementos do sistema 
console.log(`Agora sao exatamente ${hora} horas`)
if (hora > 18) { 
    console.log("Boa noite!")

} else if (hora >= 12) {
    console.log("Boa tarde!")
} else if (hora >= 6) {
    console.log("Bom dia!")
} else if (hora >= 1) {
    console.log("Boa madrugada!")
}
