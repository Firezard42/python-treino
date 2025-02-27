frase = str(input('Digite uma frase qualquer : ')).strip().replace(' ','').upper()
frase2 = frase[::-1]

print(f'O inverso de {frase} é {frase2}')
if frase == frase2:
    print('essa frase \033[0;32mÉ\033[m um políndromo')

else:
    print('essa frase \033[0;31mNÃO\033[m é um políndromo')