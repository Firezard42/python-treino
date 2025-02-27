#Removendo Palavras Irrelevantes (Stopwords)
#No PLN, algumas palavras como "o", "é", "uma" não são tão importantes. Vamos removê-las!

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#Importa a lista de stopwords (palavras irrelevantes como "o", "é", "uma", "de", "para", etc.) do NLTK.
#O nltk.corpus contém vários conjuntos de dados úteis para PLN.

stop_words = set(stopwords.words('portuguese'))
#stopwords.words('portuguese') → Pega a lista de palavras irrelevantes em português.
#set(stopwords.words('portuguese')) → Converte a lista para um conjunto (set), o que torna a busca mais rápida.

texto = "O Xurubinho é uma inteligência artificial incrível!"
tokens = word_tokenize(texto)
#faz a tokenização

tokens_filtrados = [palavra for palavra in  tokens if palavra.lower() not in stop_words]
# Usamos um list comprehension (forma compacta de criar listas em Python).
# for palavra in tokens → Percorre todas as palavras da lista.
# palavra.lower() → Converte cada palavra para minúsculas (importante porque stop_words está em minúsculas).
# if palavra.lower() not in stop_words → Mantém apenas as palavras que não estão na lista de stopwords.

print(tokens_filtrados)