try:
    a = int(input('numerador 1 : '))
    b = int(input('denominador 2 : '))
    r = a / b

except (ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')

except ZeroDivisionError:                                           #você pode ter vários excepts em um Try
    print('Não é possivel dívidir um número por zero')

except Exception as erro: #você pode usar o excet sem o Exception, porém o 'Exception as' cria uma variavel que armazena o erro nesse caso eu nomeei a variavel de erro.
    print(f'Foi encontrado o erro : {erro.__class__}') #você pode vê varias coisas do erro, aqui eu escolhi a class

else:
    print(f'Resultado é {r}')

finally:
    print('Volte sempre bixinho')