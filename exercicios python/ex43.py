peso = float(input('Qual é seu peso ?'))
altura = float(input('Qual é sua altura ?'))
imc = peso/(altura**2)

if imc < 18.5:
    print(f'Você está abaixo do peso,seu IMC é {imc:.2f}')
elif imc >= 18.5 and imc < 25:
    print(f'Você tem o peso ideal,seu IMC é {imc:.2f}')
elif imc >= 25 and imc < 30:
    print(f'Você está em sobrepeso,seu IMC é {imc:.2f}')
elif imc >= 30 and imc < 40:
    print(f'Você está em obesidade,seu IMC é {imc:.2f}')

else:
    print(f'Você está em obesidade morbida,seu IMC é {imc:.2f}')