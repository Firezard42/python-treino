#Lematização com spaCy

import spacy

nlp = spacy.load('pt_core_news_sm')
# Carregar o modelo de PLN para português


texto = "O Xurubinho está correndo atrás de comidas artificiais"

tokens = nlp(texto)
#processa o texto usando o spacy

for token in tokens:
    print(f'{token.text} -> {token.lemma_}')
    # Mostrar a palavra original e sua forma lematizada