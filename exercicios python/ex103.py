def ficha(nome = 'desconhecido',gols = ''):
    if nome == '':
        nome = 'desconhecido'
    if gols.isnumeric():
        gols = gols
    else:
        gols = 0
    print(f'O Jogador {nome} fez {gols} gol(s) no campeonato.')



nome2 =  str(input('Qual é o nome do jogador ? ')).strip()
gols2 = str(input('Quantos gols ele fez ? '))
ficha(nome2,gols2)