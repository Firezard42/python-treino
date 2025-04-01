def LeiaInt(n = 0):
    while True:
        try:
            n = int(input('Digite um número inteiro : '))
        except:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        else:
            break
    return n

def LeiaFloat(n = 0.0):
    while True:
        try: n = float(input('Digite um número real : '))

        except:
            print('\033[31mERRO: por favor, digite um número real válido.\033[m')
        else:
            break
    return n

i = LeiaInt()
r = LeiaFloat()
print(f'Número inteiro digitado foi {i} e o número real foi {r}')

