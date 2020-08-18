from nltk.corpus import words
import json
from collections import defaultdict

allowed_tlds = []
with open('domains/allowed_tld.txt', 'r') as f:
    for row in f.readlines():
        if not '--' in row:
            allowed_tlds.append(row.lower().replace('\n', ''))

with open('domains/tracked_tlds.json', 'w') as f:
    json.dump(allowed_tlds, f, indent=4)

candidate_domains = defaultdict(list)

all_words = words.words()
for index, word in enumerate(all_words):
    for domain in allowed_tlds:
        if word.lower().endswith(domain):
            front_word = word.lower().replace(domain, '')
            domain_name = f'{front_word}.{domain}'
            candidate_domains[word].append(domain_name)

            print(f'Found domain: {domain_name} - {index} / {len(all_words)}')

with open('domains/candidate_domains.json', 'w') as f:
    json.dump(candidate_domains, f, indent=4, sort_keys=True)
