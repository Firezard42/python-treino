#Se o modelo padrão não reconhecer certas entidades, podemos ensinar novas palavras ao spaCy.
import spacy
from spacy.tokens import Span

nlp = spacy.load("pt_core_news_lg")

texto = "Pessoas no Brasil usam o aplicado jubisclin para se comunicar no carnaval"
doc = nlp(texto)

nova_entidade = Span(doc,6,7,label='ORG')
doc.ents = list(doc.ents) + [nova_entidade]

for token in doc.ents:
    print(f'{token.text} -> {token.label_}')