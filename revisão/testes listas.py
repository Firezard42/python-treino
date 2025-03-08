#Listas são mutáveis
#janta = ['arroz', 'feijão', 'carne', 'suco']
# janta = list(('arroz', 'feijão', 'carne', 'suco'))
# janta.append('batata') #para adicionar elemento a lista
# janta.pop() #remove o último elemento da lista, mas você pode declarar qual posição que você que remover também.
# #del(janta[1]) #remove o elemento pela posição ou a lista inteira.
# janta.remove('arroz') #remove o elemento da lista falando o que é o elemento invés da posição.
# print(janta)

# valores = [1,5,4,2]
# valores.insert(0,5) #inseres um elemento na posição que você escolher sem remover outros.
# valores.append(7)
# valores.sort(reverse=True) #sort organiza a lista, o Reverse coloca ao contrario
# # while True:
# #     if 5 in valores: #esse loop serve pra remover todos os elementos do valor que eu quiser
# #         valores.remove(5)
# #     else:
# #         break
# print(valores)

# valores = []
# for cont in range(0,5):
#     valores.append(int(input('Digite um valor : ')))
#
# for c,v in enumerate(valores):
#     print(f'Na posição {c} encontrei {v}')

#a = [2,3,4,7]
#b = a
#b = a[:] #dessa forma você consegue criar uma copia de A para B sem uma ligação, assim você pode alterar tudo do B sem influênciar no A.
#b[2] = 8      # o A vai mudar junto com o B, pois quando você iguala uma lista na outra elas criam uma ligação e tudo que você mudar em uma, vai mudar na outra.
#print(f'Lista A : {a}')
#print(f'Lista B : {b}')

