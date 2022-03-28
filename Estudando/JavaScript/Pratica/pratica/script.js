function verificar() {
    var data = new Date()
    var idade = data.getFullYear()
    var anoa = document.querySelector('input#ano1')
    var sex = document.getElementsByName('radsex')
    var res = document.querySelector('div#res')
    var anos = idade - Number(anoa.value)
    var genero = ''
    var img = document.createElement('img')
    img.setAttribute('id', 'foto')
    if (sex[0].checked) {
        genero = 'um Homem'
        if (anos > 10 && anos <= 18) {
            img.setAttribute('src', 'eu.png')
        }
    } else if (sex[1].checked) {
        genero = 'uma Mulher'
    }
res.innerHTML = (`Voce é ${genero} com ${anos} anos de idade. `)  
res.appendChild(img) 
}
