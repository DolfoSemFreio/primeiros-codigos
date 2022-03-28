function verificar() {
    var data = new Date() // se for mexer com data precisa do new Date()
    var anoa = data.getFullYear()
    var fAno = document.querySelector('input#txtano')
    var res = document.querySelector('div#res')
    if (fAno.value.length == 0 || Number(fAno.value) > anoa ){
        window.alert('[ERRo]Verifique os dados')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = anoa - Number(fAno.value) // precisa colocar Number(x.value) quando uma pessoa que escolhe o numero a ser usado
        var genero = '' // se deixar vazio da para escolher oque voce vai colocar mais pra baixo
        var img = document.createElement('img')
        img.setAttribute('id', 'foto') // comando para adc fotos
        if (fsex[0].checked) { // checked serve para numerar a resposta quer a pessoa do site deu, exemplo o genero dela
            genero = 'Homem' 
            if(idade >=10 && idade <18 ) {
                //Adolescente
                img.setAttribute('src', 'Homem20.png') // comando para selecionar a foto que vc quer
            } else if (idade >=18 && idade <30) {
                // 20 anos
                img.setAttribute('src', 'Homem20.png')
            } else if (idade >=30 && idade < 40){
            // 30 anos
                img.setAttribute('src', 'homem30.png')
            } else if (idade >= 40) {
                // senhor
                img.setAttribute('src', 'senhor.png')
            }}       
            else if (fsex[1].checked) {
                    genero = 'Mulher'
                    if(idade >=10 && idade <18 ) {
                    //Adolescente
                    img.setAttribute('src', 'Mulheradolescente.png')
        }           else if (idade >=18 && idade <30) {
                    // 20 anos
                    img.setAttribute('src', 'Mulher20.png')
        }           else if (idade >=30 && idade < 40){
                    // 30 anos
                    img.setAttribute('src', 'mulher30.png')
        }           else if (idade >= 40) {
                    // senhor
                    img.setAttribute('src', 'senhora.png')
        }
    }
        
    }   
    res.innerHTML = `Detectamos ${genero} com ${idade}`
    res.appendChild(img)
    
}