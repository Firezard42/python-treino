# teste  = list()
# teste.append('bito')
# teste.append(20)
# galera = list()
# galera.append(teste[:]) #use [:] para copiar a lista, pois se não vai criar uma ligação.
# teste[0] = 'day'
# teste[1] = 23
# galera.append(teste[:])
# print(galera)


# galera = [['Bito',20],['Papamel',19],['Day',23],['Sweet',21]]
#
# for c in galera:
#     print(f'{c[0]} possui {c[1]} anos.')

# galera = list()
# dado = list()
# totmaior = 0
# totmenor = 0
#
# for c in range(0,3):
#     dado.append(str(input('Digite seu nome : ')))
#     dado.append(int(input('Digite sua idade : ')))
#     galera.append(dado[:])
#     dado.clear() #use para limpar a lista
#
# for c in galera:
#     if c[1] >= 21:
#         print(f'{c[0]} é maior de idade')
#         totmaior += 1
#     else:
#         print(f'{c[0]} é menor de idade')
#         totmenor += 1
#
#     print(f'existe {totmaior} pessoas maiores de idade')
#     print(f'existe {totmenor} pessoas menores de idade')
