function verificar() {
   
    var data = new Date()
    var ano = data.getFullYear()
    var nasc = document.querySelector('input#nas')
    var res = document.querySelector('div#res')
    
    if (nasc.value.length == 0 ||  Number(nasc.value) > ano) {
    window.alert = ('[ERRO] Data Invalida') }
    else {
        var sexMA = document.getElementsByName('radsex')
        var idade = ano - Number(nasc.value)
        var gênero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (sexMA[0].checked) {
            gênero = 'Homem'
            if (idade >= 10 && idade <=18) {
            img.setAttribute('src', 'eu.png')
        }   else if (idade >= 18 && idade <= 30) {
            img.setAttribute('src', 'senhor.png')
            }

        } else if (sexMA[1].checked) {
            gênero = 'Mulher'
            if (idade >= 10 && idade <= 18) {
                img.setAttribute('src', 'Mulheradolescente.png')
            } else if (idade >= 18 && idade <= 30) {
                img.setAttribute('src', 'Mulher20.png')
        }

    }
}









res.innerHTML = `Voce é <strong>${gênero}</strong> com ${idade} anos de idade`
res.appendChild(img)
}