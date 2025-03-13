# pessoas = {'nome':'Ivaldo','sexo':'M','idade': 22}
# print(f'O {pessoas['nome']} tem {pessoas['idade']} anos e é do sexo {pessoas['sexo']}')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# for k in pessoas.values():
#     print(k)
# for k in pessoas.keys():
#     print(k)
# del pessoas['sexo'] #pra apagar um item
# pessoas['nome'] = 'junin' #pra trocar um value
# pessoas['peso'] = 70.5 #pra adicionar um item (não usam append em dicionarios)
# for k,v in pessoas.items(): #primeiro é a key depois o values
#     print(f'{k} = {v}')

#brasil = []
# estado1 = {'uf':'Alagoas','sigla':'AL'}
# estado2 = {'uf':'Pernambuco','sigla':'PE'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['uf'])

# brasil = list()
# estado = dict()
# for c in range(0,3):
#     estado['uf'] =  str(input('Qual é o estado ?  '))
#     estado['sigla'] = str(input('Digite a sigla do estado : '))
#     brasil.append(estado.copy()) #pra dicionario invés de usar o [:] pra copiar você usa o copy
# for e in brasil:
#     for k,v in e.items():
#         print(f'{k} = {v}')
#     print('')

#use o itemgetter para organizar um dicionario, ele faz parte da biblioteca operator (veja o ex91)