n1 = int(input('Digite o primero número : '))
n2 = int(input('Digite o segundo número : '))
n3 = int(input('Digite o terceiro número : '))
maior = n1
menor = n1

if n2 > n1 and n2 > n3:
    maior = n2
elif n2 < n1 and n2 < n3:
    menor = n2

if n3 > n1 and n3 > n2:
    maior = n3

elif n3 < n1 and n3 < n2:
    menor = n3

elif n2 == n3 and n2 > n1:
    maior = n2
elif n2 == n3 and n2 < n1:
    menor = n2

print(f'O Maior número é {maior}\nE O Menor é {menor}')


