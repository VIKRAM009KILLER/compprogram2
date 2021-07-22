# islegaltriangle(s1, s2, s3)
# Write the function islegaltriangle(s1, s2, s3) that takes three int or float values representing
# the lengths of the sides of a triangle, and returns True if such a triangle exists and False
# otherwise. Note from the triangle inequality that the sum of each two sides must be greater
# than the third side, and further note that all sides of a legal triangle must be positive. Hint:
# how can you determine the longest side, and how might that help?

def islegaltriangle(s1, s2, s3):
	# your code goes here
	if s1 > s2:
		if s1 > s3:
			largest = s1
			a = s2
			b = s3
		else:
			largest = s3
			a = s2
			b = s1
	else:
		if s2 > s3:
			largest = s2
			a = s3
			b = s1
		else:
			largest = s3
			a = s2
			b = s1
	if a+b > largest:
		return True
	else:
		return False
	
	pass
