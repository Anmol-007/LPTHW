# mapping of states with abbreviations
states = {
	'Maharashtra': 'MH',
	'Kerala': 'KL',
	'Tamil Nadu': 'TN',
	'Himachal Pradesh': 'HP',
	'Assam': 'AS',
	'Manipur': 'MN',
	'Madhya Pradesh': 'MP',
	'Telangana': 'TG'
	}

#set of states and citites in them
cities = {
	'MH': 'Mumbai',
	'HP': 'Shimla',
	'TN': 'Chennai',
	'AS': 'Guwahati'
	}

cities['TG'] = "Hyderabad"
cities['KL'] = "Kochi"
cities['MN'] = "Imphal"
cities['MP'] = "Indore"

# print out some cities

print '-' * 12
print "MH state has: " , cities['MH']
print "TG state has:", cities['TG']

# print some states
print '-' * 12
print "Kerala's abbreviation is: ", states['Kerala']
print "Manipur's abbreviation is:", states['Manipur']

#do it by using cities and states dict
print '-' * 12
print "Tamil Nadu state has:", cities[states['Tamil Nadu']]
print "Himachal Pradesh has:", cities[states['Himachal Pradesh']]

# print every state abbreviation
print '-' * 12
for state, abbrev in states.items():
	print "%s is abbreviated as %s " % (state, abbrev)

#print every city in every state
for state, city in cities.items():
	print "%s is in %s " % (city, state)

#now do both at the same time
for state, abbrev in states.items():
	print "%s is abbreviated as %s and has %s city." % (state, abbrev, cities[abbrev])

print '-' * 12
# safely get an abbreviation by state that might not be there
state = states.get('GJ', None)

if not state:
	print "Sorry, Gujarat not here"

#get city with a default value
city = cities.get('GJ', 'Does not exist')
print "The city for the state 'GJ' is: %s." % city
