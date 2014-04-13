#Sum of squares

#Problem size
N = 100

#sum = #Using a while loop to find sum of each item squared
#summation = 0
'''counter = 1

while counter <= N:
	summation += counter**2
	counter += 1'''

#Using a for loop to create a sum of each item squared
'''for x in range(1,N+1):
	summation += x**2'''

#Using a for loop to create a list of squared items
'''sum_squares = []
for x in range(1,N+1):
	sum_squares.append(x**2)'''
	
summation = sum([elem**2 for elem in range(1,N+1)])

summation_2 = sum(range(1,N+1))**2
	
print summation_2