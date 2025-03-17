from flask import Flask, render_template
import os
import spacy
import freedictionaryapi
from collections import Counter
from freedictionaryapi.clients.sync_client import DictionaryApiClient
from freedictionaryapi.errors import DictionaryApiError
import numpy as np
from dotenv import load_dotenv

template_dir = os.path.abspath('/Users/alfredfolashade/Smart-Flashcard-Generator/Smart-Flashcard-Generator/Frontend/templates')
print(f"Looking for templates in: {template_dir}")
print(f"Directory exists: {os.path.exists(template_dir)}")

if os.path.exists(template_dir):
    print(f"Files in directory: {os.listdir(template_dir)}")
else:
    print("Directory not found!")

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('flashcard_home')

if __name__ == '__main__':
    app.run(debug=True)
    
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
clientGpt = OpenAI(api_key=api_key)

client = DictionaryApiClient()
NUM_OF_FLASHCARDS = 10

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

def get_correct_definition(word, token_context, definitions: list[freedictionaryapi.types.Definition]):
    token_context_doc = nlp(token_context)

    completion = clientGpt.beta.chat.completions.parse(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert at word sense disambiguation."},
                    {"role": "user", "content": f"""
                    I am going to give you a word along
                    with its context and some possible definitons
                    your job is to choose the most appropriate definition and return that definition only.
                    Here is the word: {word}
                    Here is the token context: {token_context}
                    Here are the definitions: {definitions}"""}
                ],
                temperature=1.0,
                
            )
            
    print(completion.choices[0].message.content)
    

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
        get_correct_definition(word, text, definitions)

    except DictionaryApiError:
        print('API error')

    
    
#print(flashcards)

client.close


