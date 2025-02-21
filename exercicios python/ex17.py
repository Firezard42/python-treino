from math import sqrt

co = float(input('Qual é o cateto oposto ? '))
ca = float(input('Qual é o cateto adjacente ? '))
h = sqrt(co**2 + ca**2)
print(f'{h:.2f}')
#A Formula pra tirar a hipotenusa do  triangulo retangulo é cateto oposto e o adjcente elevado ao quadrado somados e depois tirar a raiz dos dois numeros.
