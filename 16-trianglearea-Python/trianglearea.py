# trianglearea(s1, s2, s3)[5pts]
# Write the function trianglearea(s1, s2, s3) that takes 3 floats/ints and returns the area of the
# triangle that has those lengths of its side. If no such triangle exists, return 0. Hint: you
# will probably wish to use Heron's Formula.


def trianglearea(s1, s2, s3):
	# your code goes here
	sp = (s1 +s2 +s3)/2
	product = sp * (sp-s1) * (sp-s2) * (sp-s3)

	area = product ** (1/2)

	return area

    
	pass
