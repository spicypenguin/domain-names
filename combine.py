import json

with open('words/nouns.json', 'r') as f:
    nouns = json.load(f)

with open('words/adjectives.json', 'r') as f:
    adjectives = json.load(f)

print(len(nouns))
print(len(adjectives))
# combined = [
#     f'{adjective}{noun}'
#     for adjective in adjectives
#     for noun in nouns
#     if len(f'{adjective}{noun}') <= 15
#     and len(adjective) > 4
#     and len(noun) > 4
# ]
# print(len(combined))

# with open('words/combined.json', 'w') as f:
#     json.dump(combined, f)
