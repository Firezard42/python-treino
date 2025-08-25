#Defina uma classe que contenha pelo menos dois métodos: get_stringrecuperar uma string da entrada do console e print_stringexibir a string em letras
# maiúsculas. Além disso, inclua uma função de teste simples para validar os métodos da classe.

class InputString:

    def get_string(self):
        palavra = str(input('Digite uma frase: ')).strip()
        self.palavra = palavra


    def print_string(self):
        print(self.palavra.upper())

teste = InputString()

teste.get_string()

teste.print_string()
