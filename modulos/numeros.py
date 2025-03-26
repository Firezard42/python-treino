from pacoteExemplo import exnumeros


num = int(input('Digite um valor: '))
fat =  exnumeros.fatorial(num)
print(f'Fatorial de {num} é {fat}')
print(f'O Dobro de {num} é {exnumeros.dobro(num)}')
print(f'O Triplo de {num} é {exnumeros.triplo(num)}')