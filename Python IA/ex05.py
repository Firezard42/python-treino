#caso alguma entidade tenha marcado errado é sugerido que faça isso :
#Substituir entidades manualmente
import spacy
from spacy.tokens import Span

# Carregar o modelo spaCy
nlp = spacy.load("pt_core_news_lg")

# Texto de exemplo
texto = 'Lula troca Nísia Trindade por Alexandre Padilha no Ministério da Saúde'
doc = nlp(texto)

# Criar uma nova entidade corrigida
nova_entidade = Span(doc, 8, 11, label="ORG")  # "Ministério da Saúde" é uma organização

# Criar uma nova lista de entidades SEM a anterior
novas_entidades = [ent for ent in doc.ents if not (8 <= ent.start < 11)] + [nova_entidade]

# Substituir as entidades do documento
doc.set_ents(novas_entidades)

# Exibir entidades corrigidas
for entidade in doc.ents:
    print(f"{entidade.text} -> {entidade.label_}")