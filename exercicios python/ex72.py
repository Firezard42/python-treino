cont = ('zero','um','dois','três,','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = int(input('Digite um número entre 0 e 20 : '))
if n < 0 or n > 20:
    while n < 0 or n > 20:
        n = int(input('Numéro inválido. Digite um número entre 0 e 20 : '))

print(f'Você digitou o número {cont[n]}')