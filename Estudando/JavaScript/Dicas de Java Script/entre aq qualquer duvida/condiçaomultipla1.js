var agora= new Date()
var diaSema = agora.getDay() // getDay é dia da semana onde 0-Domingo, 1-Segunda, 2-Terça, 3-Quarta, 4-Quinta, 5-Sexta e 6-Sabado
switch(diaSema) {
    case 0:
        console.log('Domingo')
        break // break serve para ele n mandar as cases de baixo junto
        case 1:
            console.log('Segunda')
            break
            case 2:
                console.log('Terça')
                break
                case 3:
                    console.log('Quarta')
                    break
                    case 4: 
                        console.log('Quinta')
                        break
                        case 5:
                            console.log('Sexta')
                            break
                            case 6:
                                console.log('Sabado')
                                break
                                default: // default é caso nenhuma das case acima esteja correta tem casos que ele n precisa aparecer
                                    console.log('[ERRO]Dia Invalido')
                                    break                        
                        
}