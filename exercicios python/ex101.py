import datetime
def voto(ano):
    atual = datetime.datetime.now().year
    idade = atual - ano
    if idade >= 18 and idade < 65:
         return f'Com {idade} anos: Voto é obrigatorio !!!'
    elif idade < 18 and idade >= 16 or idade >= 65:
        return f'Com {idade} anos: Voto é opcional.'
    else:
        return f'Com {idade} anos: Voto é proibido.'

print(voto(int(input('Qual é sua data de nascimento ? '))))
