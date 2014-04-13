import json

file = open('restaurants.json')
output = open('group_output.json',mode='w')
jsonfile = json.loads(file.read())['Restaurants']

user_preferences = { 'price': 3, 'steak': 5, 'shakes': 10}
sum_list = []

for restaurant in jsonfile:
	summation = 0
	for name, attributes in restaurant.iteritems():
		
		for attr_name, attr_value in user_preferences.iteritems():
			if attributes.has_key(attr_name):
				summation += (attributes[attr_name]-attr_value)**2
			else:
				summation += attr_value**2
	sum_list.append((summation,restaurant))

def cmp_restaurants(a,b):
	return a[0] - b[0]

sum_list.sort(cmp=cmp_restaurants)
sum_list = [element[1] for element in sum_list]
output.write(json.dumps(sum_list))
