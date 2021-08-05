# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	if a == []:
		return True
	x = a[0]
	cs = 0
	cg = 0
	for i in range(1, len(a)):
		if a[i] < x:
			x = a[i]
			cs += 1
			continue
		if a[i] == x:
			i += 1
			continue
		if a[i] > x:
			x = a[i]
			cg += 1
			continue
	if cg == 0 or cs == 0:
		return True
	else:
		return False


	# your code goes here
	pass