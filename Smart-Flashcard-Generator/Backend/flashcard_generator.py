import spacy
from collections import Counter

NUM_OF_FLASHCARDS = 5

#load the language model
nlp = spacy.load('en_core_web_sm')


#Create an nlp object
text = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a 'batteries included' language due to its comprehensive standard library. Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[36] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2. Python consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community."
doc = nlp(text) #doc is a sequence of token objects


def preprocess_text(doc):
    """
    Preprocess function takes a doc object and 
    cleans and prepares the text for later use.

    Args:
        param1: doc object

    Returns: 
        An array fof the cleaned text
    """
    cleaned_text = []  
    for token in doc:
        if not token.is_punct:
            token = token.lemma_.lower()
            cleaned_text.append(token)

    return cleaned_text  

cleaned_text = preprocess_text(doc)
#print(cleaned_text)
word_freq = Counter(cleaned_text)
print(word_freq.most_common(NUM_OF_FLASHCARDS))
flashcards = {}
for tuple in word_freq:
    flashcards[tuple] = ""



