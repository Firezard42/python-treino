r1 = float(input('Digite a primeira reta : '))
r2 = float(input('Digite a segunda reta : '))
r3 = float(input('Digite a terceira reta : '))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    if r1 == r2 == r3:
        print('Você tem um triângulo Equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Você tem um triângulo Isósceles')
    else:
        print('Você tem um triângulo Escaleno')

else:
    print('Você não tem um triângulo')