# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	if a == []:
		return -1
	limit = 10 ** 100
	a.sort()
	for i in range(0, len(a)-1):
		for j in range(i+1, len(a)):
			m = abs(a[i] - a[j])
			if m < limit:
				limit = m
	
	return limit



	pass