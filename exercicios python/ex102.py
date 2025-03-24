def fatorial(n = 1,show = False):
    '''

    :param n: O número para ser calculado
    :param show: Mostrar ou nõo o processo do fatorial
    :return: O valor do Fatorial de n
    '''
    f = 1
    for c in range(n,0,-1):
        f = f * c
        if show == True:
            if c == 1:
                print(f'{c}  = ', end=' ')
            else:
                print(f'{c} X ',end=' ')
    return f

print(fatorial(5,True))
help(fatorial)