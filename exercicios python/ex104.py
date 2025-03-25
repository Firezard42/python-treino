def LeiaInt(num = '0'):
    if num.isnumeric():
        return num
    else:
        while True:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
            num = str(input('Digite um número : '))
            if num.isnumeric():
                break
        return num


n = LeiaInt(str(input('Digite um número : ')))
print(f'Você acabou de digitar o número {n}')