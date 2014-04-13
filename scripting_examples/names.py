#Take a file with a list of names and compute the sum of the characters multiplied by their index in the sorted list

if __name__ == '__main__':
	file = open('names.txt')
	
	#parse out any unwanted " quotations
	#split the comma seperated string of names into an list
	names = file.read().replace('"','').split(',')
	names.sort()				#sort the list alphabetically - default
	
	#iterate through the list
	#enumerate(x) returns a 2-tuple of the index and the value (index,value)
	#the 2-tuple is automatically unpackaged by the for loop using this syntax
	for index, name in enumerate(names,1):
		summation = 0
		#iterate through each character in the name string
		for character in name:
			#convert the ASCII value of the character into a position in the alphabet
			summation += (ord(character)-64)
		names[index-1] = summation*index
	
	total_sum = sum(names)
	print total_sum
	
	
	#expanded list comprehensions
	'''names = sorted(file.read().replace('"','').split(','))
	names_sum = [sum([(ord(c)-64) for c in s]) for s in names]
	positional_sum = [i*k for i,k in enumerate(names_sum,1)]
	total_sum = sum(positional_sum)
	print total_sum'''
	
	
	#one line version of the above
	#print sum([sum([(ord(c)-64) for c in s])*i for i, s in enumerate(sorted(file.read().replace('"','').split(',')),1)])
	
	file.close()