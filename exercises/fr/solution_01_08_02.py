import spacy

nlp = spacy.load("fr_core_news_sm")

text = "Apple a été créée en 1976 par Steve Wozniak, Steve Jobs et Ron Wayne."

# Traite le texte
doc = nlp(text)

# Itère sur les entités prédites
for ent in doc.ents:
    # Affiche le texte de l'entité et son label
    print(ent.text, ent.label_)
