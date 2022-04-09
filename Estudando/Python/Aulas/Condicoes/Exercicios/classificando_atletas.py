age = int(input('Qual a sua idade: '))
if age <= 9 :
    print('Voce é um atleta \033[34mMIRIM')
elif age <= 14:
    print('Voce é um atleta \033[34mINFANTIL')
elif age <= 19:
    print('Voce é um atleta \033[34mJUNIOR')
elif age <= 25:
    print('Voce é um atleta \033[34mSENIOR')
elif age > 25:
    print('Voce é um atleta \033[34mMASTER')
else:
    print('Idade invalida')