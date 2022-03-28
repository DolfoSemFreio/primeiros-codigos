function Verificar() {
    var data= new Date()
    var anoA = data.getFullYear()
    var res = document.querySelector('div#res')
    var sexMA = document.getElementsByName('radsex')
    var fAno = document.querySelector('input#data')
    var gênero = ""
    var Idade = anoA - Number(fAno.value)
    var img = document.createElement('img')
    img.setAttribute('id', 'foto')
    
    if (sexMA[0].checked) {
        gênero = "Homem"
        if (Idade >= 10 && Idade <= 18){
            img.setAttribute('src', 'eu.png')
        } else if (Idade > 18 && Idade <= 30){
            img.setAttribute('src', 'senhor.png')
        }

        
    } else if (sexMA[1].checked) {
        gênero = "Mulher"
        if (Idade >= 10 && Idade <= 18) {
            img.setAttribute('src', 'Mulheradolescente.png')
        }
        else if (Idade >= 18 && Idade <= 30) {
            img.setAttribute('src', 'Mulher20.png')
        }
        

    }





res.innerHTML = (`<p>Voce é <strong>${gênero}</strong> com ${Idade}</p>` )
res.appendChild(img)
}
