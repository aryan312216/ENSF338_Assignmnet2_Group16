import json
import random

with open('question2.json', 'r') as f:
    data = json.load(f)

# shuffle each list
for key in data:
    random.shuffle(key)

# write the shuffled lists to a new JSON file
with open('ex2.5.json', 'w') as f:
    json.dump(data,f)