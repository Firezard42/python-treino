valores = [[],[]]
for c in range(0,7):
    valor = int(input(f'Digite o {c+1}º valor : '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()
print(f'Os Valores pares digitados foram: {valores[0]}')
print(f'Os Valores ímpares digitados foram: {valores[1]}')