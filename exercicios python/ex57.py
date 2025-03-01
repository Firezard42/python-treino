sexo = str(input('Qual é seu sexo ? [M/F]')).upper().strip()
while sexo[0] != 'M' and sexo[0] != 'F':
    print('Opção incorreta, digite "M" para macho e "F" para fêmea !!! ')
    sexo = str(input('Qual é seu sexo ? [M/F]')).upper().strip()

if sexo[0] == 'M':
    print('bem vindo ao time dos macho')

elif sexo[0] == 'F':
    print('bem vinda ao time das fêmea')