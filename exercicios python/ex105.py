def notas(* num,sit = False):
    '''
    :param num: Adicionar quantas notas quiser
    :param sit: opcional,se vai mostrar ou não a situação da turma
    :return: retornar um dicionário com todos as informaçõe sobre a situação da turma
    '''
    media = 0
    quantidade = len(num)
    maior = max(num)
    menor = min(num)
    for c in num:
        media += c
    media = media/quantidade
    dic = {'total': quantidade, 'maior': maior, 'menor': menor, 'média': media}
    if sit == True:
        if media > 7:
            dic['situação'] = 'Boa'
        elif media < 7 and media >= 6:
            dic['situação'] = 'Razoavel'
        else:
            dic['situação'] = 'Ruim'
    return dic




print(notas(5,7,7,10,sit=True))
help(notas)