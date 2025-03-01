n1 = int(input('Digite um número inteiro na qual você deseja vê seu fatorial: '))
n2 = n1 - 1
fatorial = 0

for c in range(n1,0,-1):
    if c != 1:
        print(f'{c} X ',end='')
    else:
        print(f'{c} = ', end='')
    if c == n1:
        fatorial = c * n2
    else:
        fatorial = n2 * fatorial
    if n2 != 1:
        n2 = n2-1

if n1 == 1:
    fatorial = 1
    print(fatorial)

elif n1 == 0:
    fatorial = 1
    print(f'!{n1} = {fatorial}')

else:
    print(fatorial)