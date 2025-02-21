from random import shuffle

n1 = str(input('Digite o nome do primeiro aluno : '))
n2 = str(input('Digite o nome do segundo aluno : '))
n3 = str(input('Digite o nome do terceiro aluno : '))
n4 = str(input('Digite o nome do quarto aluno : '))
alunos = [n1,n2,n3,n4]
shuffle(alunos)
print(f'A ordem de apresentação do trabalho será :\n {alunos}')

# #outra alternativa, é o sorted que fica assim o cod : alunos = sorted(alunos)
# print(f'A ordem de apresentação do trabalho será :\n {alunos}')

