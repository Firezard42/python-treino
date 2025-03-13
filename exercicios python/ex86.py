matriz = [[],[],[]]
par = 0
terceira = 0
maior = 0

for c1 in range(0,3):
    for c2 in range(0,3):
        matriz[c1].append(int(input(f'Digite um valor para {c1,c2}:  ')))

for c1 in range(0,3):
        for c2 in range(0,3):
            print(f'[ {matriz[c1][c2]:^5} ]',end=' ')
            if matriz[c1][c2] % 2 == 0:
                par += matriz[c1][c2]
            if c2 == 2:
                terceira += matriz[c1][c2]
            if c1 == 1:
                if matriz[c1][c2] > maior:
                    maior = matriz[c1][c2]

        print('')

print('=-'*20)
print(f'A Soma dos números pares é {par}')
print(f'A Soma dos valores da  terceira coluna é {terceira}')
print(f'O Maior valor da segunda linha é {maior}')