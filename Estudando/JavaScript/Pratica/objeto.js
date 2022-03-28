var person = { // {} é um objeto
    firstname : 'John',
    lastName : 'Morgans',
    peso : 74.4,
    
    
    engordar(p){ // n precisa escrever function quanto esta dentro de um objeto(acredito eu)
        this.peso += p 
    }
}

person.engordar(24)
console.log(`${person.firstname} ${person.lastName} engordou ${person.peso}`) 

