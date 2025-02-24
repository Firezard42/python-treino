import math

n1 = int(input('Digite um número inteiro : '))

c = int(input('Você deseja converter esse número para \n\033[0:33m[1]\033[mBinário\n\033[0;33m[2]\033[mOctal\n\033[0;33m[3]\033[mHexadecimal\nDigite: '))

if c == 1:
    n1 = bin(n1)
    print(n1[2:])
elif c ==2:
    n1 = oct(n1)
    print(n1[2:])
elif c == 3:
    n1 = hex(n1)
    print(n1[2:])
#[2:] é pra não mostrar os prefixos
else:
    print('Opção inválida !!!')