s = float(input('Qual é o seu sálario ? '))

if s > 1250:
    a = (s*10) / 100
    print(f'Seu novo salário com o aumento de 10% agora é {s+a:.2f}')
else:
    a = (s*15) / 100
    print(f'Seu novo sálario com o aumento de 15% agora é {s+a:.2f}')