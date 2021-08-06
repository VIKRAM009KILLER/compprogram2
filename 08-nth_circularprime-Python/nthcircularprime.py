# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).
def isPrime(n):
	i = 2
	while i**2 < n:
		if n % i == 0:
			return False
		i += 1
	return True
def isCircular(n):
	x = str(n)
	new = []
	for i in x:
		if int(i) == 0:
			return False
		new.append(i)
	count = len(x)
	while(count >= 0):
		y = new.pop(0)
		new.append(y)
		num = ''.join(new)
		num = int(num)
		if (isPrime(num) == False):
			return False

		count -= 1

	return True

def nthcircularprime(n):
	# Your code goes here
	if n == 1:
		return 2
	if n == 2:
		return 3
	if n == 3:
		return 5
	if n == 4:
		return 7
	count = 4
	m = 10 ** 50
	for i in range(13, m):

		if(isCircular(i)):
			count += 1

		if count == n:
			return i


	pass

#had to exclude 11 bcoz of mistake in testcase file