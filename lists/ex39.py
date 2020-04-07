#create a mapping of state to abbreviation

states = {
    'Nairobi':'Nai',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities =  {
    'CA': 'San Franciso',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['Nai'] = 'UpperHill'

#print some cities 
print('-' * 10)
print("NY State has: ", cities['NY'])
print("Nai State has: ", cities['Nai'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is ", states['Florida'])

#do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and had city {cities[abbrev]}")

print('-' * 10)
#safely get abbreviations by state that might not be there 
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#get a city with default value 
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")