# Write the function nth_happy_number(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:

# https://en.wikipedia.org/wiki/Happy_number#:~:text=In%20number%20theory%2C%20a%20happy,starting%20with%20and%20eventually%20reaches
# Read more about the happy number from the above link.

# assert(nth_happy_number(1) == 1)
# assert(nth_happy_number(2) == 7)
# assert(nth_happy_number(3) == 10)
# assert(nth_happy_number(4) == 13)
# assert(nth_happy_number(5) == 19)
# assert(nth_happy_number(6) == 23)
# assert(nth_happy_number(7) == 28)
# assert(nth_happy_number(8) == 31)


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
		





	



def nth_happy_number(n):
	count = 0
	m = 10 ** 50
	
	for i in range(0, m):
		if(isHappy(i)):
				count += 1
		if count == n:
			return i

	return 0


