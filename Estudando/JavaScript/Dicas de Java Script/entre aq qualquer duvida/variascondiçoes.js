var idade = 17
if (idade < 16){
    console.log('Não vota')
} else { if (idade < 18 || idade > 65) { // tem como colocar "if" dentro de "else" para fazer mais condiçoes 
    console.log('Voto opcional')
}
else {
    console.log('Voto Obrigatorio')
} 
    
}