#Q7. Sort Comma-Separated Words Create a Python program that accepts a sequence of comma-separated words as input and returns
# the words sorted in alphabetical order.


#meu metodo
lista1 = str(input('Escreva um lista de frutas todas separadas por virgula: ')).split(',')
lista1.sort()

total = len(lista1)
for c in (lista1):
    if c == lista1[total-1]:
        print(c)
    else:
        print(c,end=',')



#metodo gpt
lista1 = input('Escreva uma lista de frutas todas separadas por vírgula: ').split(',')
lista1.sort()
print(','.join(lista1))