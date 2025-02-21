n = str(input('Digite o seu nome completo : '))
print(n.upper()) #tudo maisculo
print(n.lower()) #tudo minusculo
n2 = n.replace(' ','') #para remover  os espaços do nome
print(len(n2))
n3 = n.split() #para dividir uma str em listas (o caracter sliptador é os espaços)
print(len(n3))