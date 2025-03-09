import spacy
import freedictionaryapi
from collections import Counter
from freedictionaryapi.clients.sync_client import DictionaryApiClient
from freedictionaryapi.errors import DictionaryApiError

client = DictionaryApiClient()
NUM_OF_FLASHCARDS = 5

#load the language model
nlp = spacy.load('en_core_web_lg')


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

def get_correct_definition(token_context, definitions: list[freedictionaryapi.types.Definition]):
    token_context_doc = nlp(token_context)
    token_context_cleaned = preprocess_text(token_context_doc)
    token_context_vectors = []
    n=0
    sum_of_vectors=0
    for token in token_context_cleaned:
        token_context_vectors.append(nlp(token).vector)
        sum_of_vectors=sum_of_vectors+nlp(token).vector
        n=n+1
    token_context_agg = sum_of_vectors/n
    
        

    definitions_dict ={}
    for definition in definitions:  
        definition_str: str = str(definition)
        definition_doc = nlp(definition_str)    
        definitions_dict.update({definition_str : token_context_doc.similarity(definition_doc)})
       
    max_score=0.0
    for definition, score in definitions_dict.items():
        if(score>max_score):
            correct_definition=definition       
            max_score=score
    
    return correct_definition
    
    
    


most_common_words = most_frequent_words(cleaned_text)
print(most_common_words)
flashcards= []
for word, count in most_common_words:
    try:
        parser = client.fetch_parser(word)
        phrase = parser.word
        meanings: list[freedictionaryapi.types.Meaning] = phrase.meanings
        for meaning in meanings:
            definitions: list[freedictionaryapi.types.Definition] = meaning.definitions
        print(get_correct_definition("python is my favourite progamming language I use to release new code", definitions)) 

    except DictionaryApiError:
        print('API error')

    
    
#print(flashcards)



client.close
