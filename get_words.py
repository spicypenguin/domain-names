import nltk
from nltk.corpus import words
import json
import re

nouns = set()
adjectives = set()

tagged_words = nltk.pos_tag(words.words())

for index, word in enumerate(tagged_words):
    if re.match('^[a-zA-Z]+$', word[0]):
        if word[1] == 'NN':
            nouns.add(word[0].lower())
        elif word[1] == 'JJ':
            adjectives.add(word[0].lower())

with open('words/nouns.json', 'w') as f:
    json.dump(list(nouns), f)

with open('words/adjectives.json', 'w') as f:
    json.dump(list(adjectives), f)
