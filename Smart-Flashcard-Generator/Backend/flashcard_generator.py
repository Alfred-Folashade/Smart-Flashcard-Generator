from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import spacy

from collections import Counter

import numpy as np
from dotenv import load_dotenv
import secrets
from flask_wtf import FlaskForm, CSRFProtect
import asyncio
from googletrans import Translator
import json
import re

app = Flask(__name__)
CORS(app)








    
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI
client = OpenAI(api_key=api_key)


NUM_OF_FLASHCARDS = 4

LANGUAGE_MODELS = {
    'English': 'en_core_web_lg',
    'Spanish': 'es_core_news_lg',
    'French': 'fr_core_news_sm',
}

#load the language model
nlp = spacy.load('en_core_web_lg')


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
        if not token.is_punct and not token.is_stop and token.is_alpha:
            token = token.lemma_.lower()
            cleaned_text.append(token)

    return cleaned_text  



def most_frequent_words(text):
    word_freq = Counter(text)
    most_common_words = word_freq.most_common(NUM_OF_FLASHCARDS)
    return most_common_words

def get_correct_definition(words: list[str], token_context):

    prompt = f"""
    I am going to give you a list of words along with their context.
    Your job is to choose the most appropriate but simple English definition in addition with translations where appropriate that would be suitable for a language learner and return the definitions
    as a JSON array of objects, where each object has "word" and "definition". Do not include any other text.
    Here are the words:
    {words}
    Here is the context:
    {token_context}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert at word sense disambiguation."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5
    )

    content = response.choices[0].message.content

    # Clean up any Markdown code block formatting
    cleaned_content = re.sub(r"^```(?:json)?|```$", "", content.strip(), flags=re.MULTILINE).strip()

    try:
        return json.loads(cleaned_content)
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON response.")
        print("Raw content was:", cleaned_content)
        return None
    
def generate(text, language):
    #Create an nlp object
    #text = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a 'batteries included' language due to its comprehensive standard library. Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0.[36] Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2. Python consistently ranks as one of the most popular programming languages, and has gained widespread use in the machine learning community."
    #load the language model
    nlp = spacy.load(LANGUAGE_MODELS.get(language))
    doc = nlp(text) #doc is a sequence of token objects
    cleaned_text = preprocess_text(doc)
    most_common_words = most_frequent_words(cleaned_text)
    print("word", most_common_words)
    flashcards= {}
    flashcards = get_correct_definition

    return flashcards



    
#print(flashcards)


@app.route('/read-formtext', methods=['POST'])
def read_formtext():
    data = request.get_json()
    text = data.get('text')
    language = data.get('language')
    print(language)
    print(text)
    flashcard_dicts = {}
    flashcard_dicts= generate(text, language)
    print(flashcard_dicts)
   
    return jsonify(flashcard_dicts)  

if __name__ == '__main__':

    app.run(debug=True)
    
client.close


