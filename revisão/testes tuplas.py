#Tuplas são imútaveis
from operator import index

#pessoas = ('Carlos','João','Amaro','Maria','Junior')
# print(sorted(pessoas)) #sorted deixa as tuplas em ordem alfabetica

# for pos,c in enumerate(pessoas):
#     print(f'{c} na posição {pos}')

# for c in range(0,len(pessoas)):
#     print(f'{pessoas[c]} na posição {c}')

# a = (1,5,8)
# b = (2,5,7,1)
# c = a+b #tuplas não vão somar os números e sim juntar todos em uma tupla maior, e a sequencia de a+b ou b+a importa na sequencia da tupla
# print(c)
# print(c.index(5,2))
#.count serve pra contar quantos desse elemento tem na tupla
#.index é onde esse elemento apareceu pela primeira vez e usando uma "," dentro do index você pode escolher de apartir de qual elemento vai começar a busca

# pessoa = ('Ivaldo',22,'M',68.9) #Você pode ter dados de vários tipos dentro de uma tupla
# del(pessoa) #Você pode apagar uma tupla por completa (obs: você NÃO pode apagar apenas um item da tupla, apenas ela por completo)
# print(pessoa)

