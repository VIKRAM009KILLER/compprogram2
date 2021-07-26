"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	# Your code goes here
	if len(array) <= 1:
		return array
	pivot = array.pop()
	list_small = []
	list_greater = []

	for i in array:
		if i < pivot:
			list_small.append(i)
		else:
			list_greater.append(i)

	return quicksort(list_small) + [pivot] + quicksort(list_greater)
    
	pass