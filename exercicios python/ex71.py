print('='*40)
print('\033[34mBANCO DO JAVALI\033[m'.center(45))
print('='*40)
n = int(input('Qual valor você que sacar ? R$'))
n2 = n
ced = 50
n3 = 0
print('-'*20,'SACADO'.center(20),'-'*20)
while True:
    if n2 >= ced:
        n2 = n2-ced
        n3 += 1
    else:
        if n3 > 0:
            print(f'{n3} cédulas de \033[32m{ced}R$\033[m')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        n3 = 0
        if n2 == 0:
            break

