# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
	num = abs(n)

	na = []

	while(num != 0):
		na.append(num%10)
		num = num // 10

	if k <= len(na)-1:
		na[k] = d
		fnum = 0
		for i in range(len(na)):
			fnum = fnum + na[i]*10**i



	else:
		x = 10 ** k
		fnum = x + abs(n)
		if n < 0:
			fnum = -1 * fnum


	return fnum

