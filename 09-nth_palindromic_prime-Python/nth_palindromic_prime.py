# Write the function fun_nth_palindromic_prime(n) that takes 
# a non-negative int n and returns the nth palindromic Prime, 
# which is a palidrome number such that 
# it is also a prime. 

# For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) 
# returns 2
def isPal(n):
	x = str(n)
	y = x[::-1]
	if x == y:
		return True
	return False

def isPrime(n):
	if n <= 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True
def fun_nth_palindromic_prime(n):
	if n == 0:
		return 2
	if n == 1:
		return 3
	if n == 2:
		return 5
	if n == 3:
		return 7
	count = 3
	m = 10 ** 50
	for i in range(11, m):
		if(isPal(i)):
			if(isPrime(i)):
				count += 1

		if count == n:
			return i
	
	return 0