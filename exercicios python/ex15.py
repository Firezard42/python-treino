km = float(input('Quantos KM foram percorridos ? '))
dias = int(input('Quantos dias o carro foi alugado ? '))
valor = (dias*60) + (km*0.15)
print(f'Você deve pagar R$ {valor:.2f} !!!')