n1 = int(input('Digite o primeiro número inteiro : '))
n2 = int(input('Digite o segundo número inteiro : '))

if n1 > n2:
    print(f'{n1} é o maior número')
elif n2 > n1:
    print(f'{n2} é o maior número')

else:
    print('Os Dois números são iguais.')
