from  time import sleep
def maior(* num):
    tam = len(num)
    print('=-' * 20)
    print('Analisando os valores passados...')
    if tam == 0:
        print('Nenhum valor foi passado.')
    else:
        for c in num:
            print(c,end=' ')
            sleep(0.3)
        print(f'foram informados {tam} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
    print('=-' * 20)



maior(2,5,9,7,6,2)
maior()