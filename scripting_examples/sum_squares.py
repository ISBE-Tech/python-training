#Take the difference between the square of sums and the sum of squares for N = 100

if __name__ == '__main__':
	#define problem size
	N = 100
	
	sum_of_squares = sum([k**2 for k in range(1,N+1)])
	square_of_sums = sum(range(1,N+1))**2
	summation = square_of_sums - sum_of_squares
	
	#alternatively there are sum equations that can be used without looping
	#print (N*(N+1)/2)**2 - N*(N+1)*(2*N+1)/6
	
	print summation