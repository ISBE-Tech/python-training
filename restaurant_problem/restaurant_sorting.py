#python program implementing restaurant sorting algorithm
import json
import sys

if __name__ == '__main__':
	jsonfile = open('restaurants.json')
	restaurants = json.loads(jsonfile.read())['Restaurants']
	jsonfile.close()
	sortedrestaurants = []
	userrequest = {'price': 0,'steak': 5, 'shakes': 10, 'delivery': 0, 'pizza': 0, 'chicken': 0, 'mexican': 0, 'juice': 0, 'asian': 0}
	cmd_io = True
	
	if cmd_io:
		sys.stdout.write('\n')
		for k in userrequest:
			userrequest[k] = float(raw_input("What range of %s do you prefer (0-10): " % k))%10
		sys.stdout.write('\n')
	
	oprestaurant = opsum = float("inf")
	for restaurant in restaurants:
		sum = 0
		for name, attributes in restaurant.items():
			for attrib, value in userrequest.items():
				if attributes.has_key(attrib): 
					sum += (value*((attributes[attrib]/10) - 1))**2
				else:
					sum += value**2
		
		sortedrestaurants.append((sum, restaurant))
		if sum < opsum: 
			oprestaurant = restaurant
			opsum = sum
	
	def cmp_restaurants(a, b):
		return -1 if a[0] < b[0] else 1 if a[0] > b[0] else 0
	
	sortedrestaurants.sort(cmp_restaurants)
	#sortedrestaurants = [k[1] for k in sortedrestaurants]
	
	if not cmd_io:
		output = open('user_response.json', 'w')
		output.write(json.dumps(sortedrestaurants))
		output.close()
	else:
		print sortedrestaurants
	