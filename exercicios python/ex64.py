n1 = 0
cont = 0
soma = 0
while n1 != 999:
    n1 = int(input('Digite um número inteiro (\033[31mse quiser parar digite 999\033[m) : '))
    if n1 != 999:
        cont += 1
        soma = soma+n1
    else:
        print('FIM.')

print(f'numeros digitado : {cont}')
print(f'Soma : {soma}')