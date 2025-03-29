def leiadinheiro(n = ''):
    while True:
        n2 = str(input(f'{n}'))
        n2 = n2.replace(',','.')
        n3 = n2.replace('.','')
        if n3.isnumeric():
            n2 = float(n2)
            return n2
        else:
            print(f'\033[31mERROR: "{n2}" é um valor inválido.\033[m')
