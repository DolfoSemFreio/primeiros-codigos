function carregar() {
var msg = window.document.getElementById('msg')
var img = window.document.getElementById('imagem')
var data = new Date()
var hora = data.getHours()
// var hora = 19

msg.innerHTML = `Agora são ${hora} horas.`
if (hora >= 0 && hora <12) {
    img.src = 'manha.png' // pra adc imagem é esse comando e o id da imagem
    document.body.style.background = '#ffc298' // esses codigos sao codigos de cores pegados no photoshop
} else if (hora >=12 && hora <= 18) {
    img.src = 'Tarde.png'
    document.body.style.background ='#e2631d'

} else {
    img.src = 'noite.png'
    document.body.style.background ='#245790'

}



}