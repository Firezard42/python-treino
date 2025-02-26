print('='*12,'SUPERLASCADO','='*12)
n1 = float(input('Qual é o preço das compras ? '))

print('FORMAS DE PAGAMENTO')
n2 = int(input('[1]à vista dinheiro/cheque\n[2]à vista cartão\n[3]2x cartão\n[4]3x ou mais no cartão\nQual é sua opção : '))
if n2 == 1:
    desconto = n1 - (n1*10)/100
    print(f'Desconto de 10% adicionado, valor total das compras : R${desconto:.2f}')

elif n2 == 2:
    desconto = n1 - (n1*5)/100
    print(f'Desconto de 5% adicionado, valor total das compras : R${desconto:.2f}')

elif n2 == 3:
    print(f'O Valor total das compras: R${n1:.2f}')

elif n2 == 4:
    juros = n1 + (n1*20)/100
    print(f'Juros de 20% adicionado, valor total das compras : R${juros:.2f}')

else:
    print('\033[0;31mOPÇÃO INVÁLIDA !!!\033[m')
