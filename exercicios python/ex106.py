from time import sleep

c = ( '\033[m',  #0 - sem cores
      '\033[0;41m', #1 vermelho
        '\033[0;42m', #2 verde
        '\033[0;43m', #3 amarelo
        '\033[0;44m', #4 azul
        '\033[0;45m', #5 roxo
        '\033[0;46m', #6 ciano
        '\033[7m') #7 branco


def ajuda(n,cor = 0):
    sleep(0.5)
    print(c[cor],end='')
    help(n)
    print(c[0],end='')


def decoracao(n,cor = 0):
    n2 = len(n)+4
    sleep(0.5)
    print(c[cor],end='')
    print('~' * n2)
    print(n.center(len(n)+4))
    print('~' * n2)
    print(c[0],end='')
    sleep(0.5)


while True:
    decoracao('SISTEMA DE AJUDA PyHELP',2)
    help1 = str(input(f'{c[3]}Função ou biblioteca >{c[0]} ')).strip()
    help2 = help1.upper()
    if help2 == 'FIM':
        break

    decoracao(f'Acessando o manual do comando "{help1}"',4)

    ajuda(help1,7)


decoracao('ATÉ LOGO!',1)
