n1 = int(input('Digite um número inteiro na qual você deseja vê seu fatorial: '))
n2 = n1
fatorial = 0
print(f'{n1}! = ',end='')
while n2 != 1 and n2 != 0:
    print(f'{n2} X ',end='')
    n2 -= 1
    if n2 == n1-1:
        fatorial = n1 * n2
    else:
        fatorial = fatorial * n2

if fatorial == 1 or fatorial == 0:
    print(f'{n1} = 1')

else:
    print(f'1 = {fatorial}')