def LeiaInt(n = ''):
    while True:
        try:
            n2 = int(input(f'{n}'))
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            break
    return n2

def Linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(Linha())
    print(f'{txt}'.center(42))
    print(Linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for c2 in lista:
        print(f'\033[33m{c}\033[m - \033[34m{c2}\033[m')
        c += 1
    print(Linha())
    while True:
        r = LeiaInt('\033[33mDigite sua opção :\033[m ')
        if r > len(lista) or r < 1:
            print('\033[31mOPÇÃO INVÁLIDA.\033[m')
        else:
            break
    return r




