#Tokenização: Separando um Texto em Palavras
#A tokenização divide um texto em palavras individuais. Isso é essencial para análise de linguagem!


from nltk.tokenize import word_tokenize

texto = "O Xurubinho é uma inteligência artificial incrível!"
tokens = word_tokenize(texto) #responsavel pela tokenização do texto

print(tokens)
