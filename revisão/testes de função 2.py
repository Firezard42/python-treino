# def contador(i,f,p):
#     #pra criar uma docstringer você deve criar ''' áspas embaixo do def
#     '''
#     :param i: ínicio do contador
#     :param f: Fim do contador
#     :param p: passo a passo do contador
#     :return: sem return
#     função criada por Ivaldo Netto
#     '''
#     c = i
#     while c <= f:
#         print(f'{c}',end='..')
#         c += p
#     print('FIM!')
#
# contador(1,10,2)
# help(contador)            #duas formas de chamar ajuda interativa atraves do help ou do doc
# print(contador.__doc__)

# def soma(a = 0,b = 0,c = 0): #argumentos opcionais, ex se alguém não declarar c ele vai valer 0 e não vai dar erro
#     s = a+b+c
#     print(f'A Soma de todos valores é {s}')
#
# soma(1,2)

# def teste(b):
#     a = 8
#     b = b+5 #você só pode usar as váriaveis que você declarar de forma interna no escopo local.
#     print(f'a no escopo local : {a} ')
#     print(f'b no escopo global : {b}')
#
# a = 2
# teste(a)
# print(f'a no escopo global : {a}')

#def teste(b):
    #global a #isso faz qualquer modificação que você fizer no escopo local em uma variavel global continuar global, diferente do exemplo de cima que criava duas variaveis a
#     a = 8
#     b = b+5
#     print(f'a no escopo local : {a} ')
#     print(f'b no escopo global : {b}')
#
# a = 2
# teste(a)
# print(f'a no escopo global : {a}')

# def soma(a = 0,b = 0, c = 0):
#     s = a+b+c
#     return s #usando o return o valor de s vai retornar para o que for colocado antes da chamada da função
#
# r1 = soma(1,2,3)
# r2 = soma(2,1)
# r3 = soma(9)
# print(f'Os Valores são {r1},{r2} e {r3}')
# print(soma()) #você pode da um print direto se quiser

# def fatorial(n = 1):
#     f = 1
#     for c in range(n,0,-1):
#         f = f * c
#     return f #você também pode usar o return pra outras coisas além de números.
#
# n2 = int(input('Você deseja vê qual fatorial ? '))
# print(f'A fatorial de {n2} é {fatorial(n2)}')

# def teste(p):
#     if p % 2 == 0:
#         return 'o número é par'
#     else:
#         return 'o número é impar'
#
# print(teste(2))

# def teste(p):
#     if p % 2 == 0:
#         return True
#     else:
#         return False
#
# if teste(3):
#     print('par')
# else:
#     print('impar')