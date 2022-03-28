let num = [10 ,11 ,12 ,13 ,14 ,15 ,16]
num.sort() // colocar em ordem crescente
num.push(1) // adiciona o valor na ultima casa

console.log(num)
console.log(`O vetor tem ${num.length} elementos`) // length vai mostrar quantas casas ele tem
console.log(`O primeiro valor do vetor é ${num[0]}`) // se colocar esse zero do lado significa que ele vai mostrar o primeiro valor do array
let pos = num.indexOf(10) // ele procura o numero e te da a localização dele dentro do array
if (pos == -1) {
    console.log(`O valor nao foi encontrado`)
   } else {
       console.log(`O valor esta na posição ${pos}`)
   }
 


