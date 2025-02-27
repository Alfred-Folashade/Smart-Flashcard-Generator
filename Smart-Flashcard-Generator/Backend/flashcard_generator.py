import spacy

NUM_OF_FLASHCARDS = 5

#load the language model
nlp = spacy.load('en_core_web_sm')
NER = spacy.load("en_core_web_sm")

#Create an nlp object
text = "Einstein is a brilliant scientist from Germany"
doc = nlp(text)
doc_ner = NER(text)
#Part of speech tagging

for token in doc:
    print(token.text, token.pos_, token.lemma_)


#Named entity recognition
"""
for ent in doc_ner.ents:
    print(ent.text, ent.label_)
"""