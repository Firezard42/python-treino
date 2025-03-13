jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Qual é o nome do jogador ? ')).strip().capitalize()
p = int(input('Quantas partidas ele jogou ? '))
for c in range(0,p):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
for c in gols:
    total += c
jogador['gols'] = gols
jogador['total'] = total
print(jogador)
print('=-'*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print('=-'*30)
print(f'O Jogador {jogador['nome']} jogou {p} partidas.')
for e,c in enumerate(jogador['gols']):
    print(f'=> Na partida {e}, fez {c} gols')
print(f'Foi um total de {jogador['total']} gols.')