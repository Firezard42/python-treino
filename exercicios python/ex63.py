n = int(input('Digite um número inteiro : '))
n2 = 0
n3 = 0
n4 = 1
n5 = 0

while n2 != n:
    n5 = n3 + n4
    n3 = n4
    n4 = n5
    n2 = n2+1
    if n2 != n:
        print(f'{n5} ', end=' -> ')
    else:
        print(f'{n5} ', end='  ')