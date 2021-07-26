# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.


def digilist(n):
	a = []
	while(n != 0):
		m = n % 10
		a.append(m)
		n = n // 10
	
	a.sort()
	
	
	return a




def mostfrequentdigit(n):

	# your code goes here
	if n < 10:
		return n
	digits = digilist(n)
	
	
	freq = {}
	

	for i in digits:
		freq[i] = digits.count(i)

	m = max(freq.values())
	
	

	for key, value in freq.items():
		if value == m:
		    mfd = key
		    return mfd

	
	





    

		




	pass