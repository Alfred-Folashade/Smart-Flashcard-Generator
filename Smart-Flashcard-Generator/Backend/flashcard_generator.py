import spacy
from collections import Counter
from freedictionaryapi.clients.sync_client import DictionaryApiClient
from freedictionaryapi.errors import DictionaryApiError

client = DictionaryApiClient()
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
        if not token.is_punct and not token.is_stop:
            token = token.lemma_.lower()
            cleaned_text.append(token)

    return cleaned_text  

cleaned_text = preprocess_text(doc)

def most_frequent_words(text):
    word_freq = Counter(text)
    most_common_words = word_freq.most_common(NUM_OF_FLASHCARDS)
    return most_common_words

def get_correct_definition(token_context, meanings):
    token_context_doc = nlp(token_context)
    
    definitions_dict ={}
    for definition in meanings.definitions:
        definition_doc = nlp(definition)
        definitions_dict.update(definition, token_context_doc.similarity(definition_doc))
    
   
    max_score=0.0

    for definition, score in definitions_dict.items:
        if(score>max_score):
            correct_definition=definition
            max_score=score
    
    return correct_definition
    
    
    


most_common_words = most_frequent_words(cleaned_text)
print(most_common_words)
flashcards= []
for word in most_common_words:
    try:
        
        parser = client.fetch_parser(word[0])
        phrase = parser.word
        print(phrase.word , parser.get_all_definitions())
    except DictionaryApiError:
        print("Api error")
#print(flashcards)




