jogadores = []
dados = {}
gols = list()
total = 0
while True:
    dados['nome'] = (str(input('Qual é o nome do jogador ? ')))
    p = int(input('Quantas partidas ele jogou ? '))
    for c in range(0,p):
        gol = int(input(f'Quantos gols na partidas {c}? '))
        total += gol
        gols.append(gol)
    dados['gols'] = gols[:]
    dados['total'] = total
    jogadores.append(dados.copy())
    dados.clear()
    gols.clear()
    total = 0
    cont = str(input('Quer continuar ? [S/N] ')).strip().upper()
    while cont not in 'SN':
        cont = str(input('\033[31mOPÇÃO INVÁLIDA\033[m.Quer continuar ? [S/N] ')).strip().upper()
    if cont == 'N':
        break
print('=-'*30)
print(f'\033[34m{'Cod'}   {'Nome':<15} {'Gols':^13} {'Total':>12}\033[m')
for e,c in enumerate(jogadores):
    print(f'{e}    {c['nome']:<15} {str(c['gols']):^15} {c['total']:>10}')
print('=-'*30)
while True:
    dados2 = int(input('Digite o cod do jogador que você deseja vê os dados(999 para): '))
    while dados2 >= len(jogadores) and dados2 != 999:
        dados2 = int(input('\033[31mOPÇÃO INVÁLIDA\033[m.Digite o cod do jogador que você deseja vê os dados(999 para): '))
    if dados2 == 999:
        break
    print(f'--- > Levantamento do jogador {jogadores[dados2]['nome']}')
    for e,c in enumerate(jogadores[dados2]['gols']):
        print(f'--- No jogo {e} fez {c} gols.')

