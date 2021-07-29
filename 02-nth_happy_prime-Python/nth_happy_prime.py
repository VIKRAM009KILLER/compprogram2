# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def isPrime(n):
	if n <= 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

def digilist(n):
	dlist = []
	while(n != 0):
		d = n % 10
		n = n // 10
		dlist.append(d)
	return dlist



def isHappy(n):
	num = digilist(n)
	newnum = sum(map(lambda i : i * i, num))
	
	while (newnum > 0):
		num = digilist(newnum)
		newnum = sum(map(lambda i : i * i, num))
		if newnum == 1:
			return True
		if newnum < 10:
			return False
		




def fun_nth_happy_prime(n):
	count = 0
	m = 10 ** 50
	if n == 0:
		return 7
	for i in range(8, m):
		if(isPrime(i)):
			if(isHappy(i)):
				count += 1
		if count == n:
			return i

	return 0