# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).
def isPronic(n):
	new = []

	for i in range(1, n):
		if n % i == 0:
			new.append(i)
	new.sort()
# 	print(new)
	for j in range(len(new)-1):
		for k in range(j+1, len(new)):
			if(new[k] == new[j] + 1):
			    if new[k] * new[j] == n:
			        return True
	return False


def nthpronicnumber(n):
	# Your code goes here
	m = 10 ** 50
	if n == 0:
	    return 0
	if n == 1:
	    return 2
	count = 1

	for i in range(3, m):
	    if(isPronic(i)):
	        count += 1
	    if count == n:
	        return i
			
			
# print(nthpronicnumber(3))
# print(isPronic(6))
	pass