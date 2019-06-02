states = {
    'Oregon' : 'OR',
    "Florida": 'FL',
    "New York": 'NY',
    'California': 'CA',
    "Michigan": 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': "Fort Lauderdal"
}

cities["NY"] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abgreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")

city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is : {city}")