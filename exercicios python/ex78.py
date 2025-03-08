valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para posição {c} : ')))
print('='*45)
print(f'Você digitou os valores {valores}')

maior = max(valores)
menor = min(valores)
print(f'O Maior número foi {maior} na posição',end=' ')
for c,v in enumerate(valores):
    if v == maior:
        print(c,end=' ')
print('')

print(f'O Menor número foi {menor} na posição',end=' ')
for c,v in enumerate(valores):
    if v == menor:
        print(c,end=' ')