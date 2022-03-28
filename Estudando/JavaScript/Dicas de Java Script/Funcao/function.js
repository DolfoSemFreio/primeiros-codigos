function parimp(n) { // o n la dentro é o parâmetro e o parimp é a chamada
    if (n%2==0) { // isso é a ação
        return  'par' // dps do return só colocar aspas e boa
    } else {
        return 'impar' // return é o retorno
    }

}
let res = parimp(123) // o 12 é o valor do parâmetro, claro que ele pode mudar
console.log(`O numero é ${res}`) // da pra fazer isso direto sem precisar da variável

