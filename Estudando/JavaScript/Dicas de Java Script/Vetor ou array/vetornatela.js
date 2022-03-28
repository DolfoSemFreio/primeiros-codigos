let valores = [9 , 5 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
valores.sort()
/*for (let pos=0;pos <valores.length; pos++) { // é a mesma coisa que o de baixo
    console.log(`A posição ${pos} tem o valor ${valores[pos]}`)
}*/
for(let pos in valores) { // usado em variáveis compostas 
    console.log(`A posicao ${pos} tem o valor ${valores[pos]}`)
}