def decoracao(n):
    n2 = len(n)+2
    print('~' * n2)
    print(n.center(len(n)+2))
    print('~' * n2)


while True:
    print('\033[0;42m')
    decoracao('SISTEMA DE AJUDA PyHELP')
    print('')
    print('\033[m')
    help1 = str(input('Função ou biblioteca > ')).strip()
    help2 = help1.upper()
    if help2 == 'FIM':
        break
    print('\033[0;44m')
    decoracao(f'Acessando o manual do comando "{help1}"')
    print('')
    print('\033[m')

    print('\033[7m')
    help(help1)
    print('')
    print('\033[m')
print('\033[0;41m')
decoracao('ATÉ LOGO!')
print('')
print('\033[m')
