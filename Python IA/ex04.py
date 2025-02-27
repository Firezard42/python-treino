#Código para Reconhecimento de Entidades

import spacy

nlp = spacy.load('pt_core_news_sm')

texto = 'Elon Musk discute sanções a Alexandre de Moraes: “Tem bens nos EUA?”'

tokens = nlp(texto)

for token in tokens.ents:
    print(f'{token.text} -> {token.label_} ')
# Exibir entidades encontradas
