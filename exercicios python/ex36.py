print('-'*12,'\033[0;34mBANCO DO JAVALI\033[m','-'*12)

valor = float(input('Qual é o valor da casa ? '))
salario = float(input('Qual é seu sálario ? '))
anos = float(input('Em Quantos anos você pretende pagar essa casa ? '))

mensalidade = valor / (12*anos)
porcentagem = 30*salario / 100

if mensalidade > porcentagem:
    print(f'A Mensalidade é {mensalidade:.2f}R$ sendo assim é superior a 30%.\n\033[0;31mEMPRESTIMO NEGADO !!!\033[m')

else:
    print(f'A Mensalidade será {mensalidade:.2f}R$.\n\033[0;32mEMPRESTIMO APROVADO !!!\033[m')