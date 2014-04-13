
file = open('names.txt')
names = file.read()
names = names.replace('"','')
names_list = names.split(',')
names_list.sort()
names_sum = []


for index, name in enumerate(names_list,1):
	summation = 0
	for character in name:
		summation += ord(character) - 64
	names_sum.append(summation*index)

total_sum = sum(names_sum)
print total_sum
	
file.close()