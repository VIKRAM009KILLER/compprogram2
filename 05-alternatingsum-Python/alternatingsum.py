# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.




def fun_alternatingsum(a):

	if a == []:
	    return 0

	num = a.pop(0)
	new = []
	for i in a:
	    i = i * -1
	    new.append(i)
	    
# 	print(new)

	return num + + fun_alternatingsum(new)


