import json


with open('states.json') as f:
    country = json.load(f)

for state in country['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(state, f, indent=2)

print(type(state))
