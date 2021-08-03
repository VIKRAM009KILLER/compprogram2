# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	p = len(L)
	q = len(L[0])
	new = []
	for i in range(0, p):
		for j in range(0, q):
			value1 = L[i][j]
			print(value1)
			new.append(value1)
	for i in new:
	    c = new.count(i)
	    if c > 1:
	        return True
			
			
	return False

			

	return False