# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	if a == []:
		return None
	if len(a) == 1:
		return a[0]
	if len(a) % 2 == 0:
		n = len(a) // 2
		i = n-1
		j = n
		m = (a[i]+a[j]) / 2

	else:
		n = len(a) // 2
		m = a[n]

	return m
	pass