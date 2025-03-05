from time import perf_counter

while True:
    tabuada = int(input('Que vê a tabuada de qual valor ? '))
    if tabuada < 0:
        break
    else:
        for c in range(1,11):
            print(f'{tabuada} X {c:2} = {tabuada*c}')

print('FINALIZANDO PROGRAMA...')
