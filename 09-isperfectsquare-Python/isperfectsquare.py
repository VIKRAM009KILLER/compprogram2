# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.
import math

from attr import validate

def isperfectsquare(n):
	# your code goes here
	try:
		num = int(n)
	except ValueError:
		return False
			
		
	if num < 0:
		return False
	# num = int(n)
	

	m = int(math.sqrt(num))

	

	if (m ** 2 == num):
		return True
	else:
		return False
	pass
