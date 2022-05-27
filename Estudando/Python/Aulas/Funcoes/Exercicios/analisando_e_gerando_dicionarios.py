def notas(* num, sit=False):
    """Mostra a media de notas e a situacao do aluno

    Args:
        sit (bool, optional): Escolhe se deseja ou nao mostrar a situacao do aluno. Defaults to False.

    Returns:
        _type_: Retorna um dicionario
    """
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['media'] = sum(num) / len(num)
    if sit:
        if r['media'] <= 3:
            r['situacao'] = 'RUIM'
        elif r['media'] >= 6:
            r['situacao'] = 'RAZOAVEL'
        elif r['media'] == 10:
            r['situacao'] = 'MUITO BOA'
    
    return r  
    

# Programa principal
resp = notas(10, 10, 10 )
print(resp)