# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def Rotate(a):

	b = str(a)
	new = []
	for i in b:
		new.append(i)
	news= ""
	if len(new) % 2 == 0:
		n = len(new)//2
		p = new[:n]
		q = new[n:]
		res1 = ''.join(p)
		res2 = ''.join(q)

		news += res2 + res1
		

		return news
	else:
	    l = len(new)
	    d = new.pop(0)
	    new.append(d)
	    res = ''.join(new)
	    return res


		

def isrotation(x, y):
	# Your code goes here
	count = 0
	x = str(x)
	y = str(y)
	if(x[::-1] == y):
	    return True
	if len(x) != len(y):
		return False
	if x == y:
		return True
	while(count <= len(x)):
		p = Rotate(x)
		print(p)
		count += 1
		if p == y:
			return True
		x = p

	return False

	

	pass