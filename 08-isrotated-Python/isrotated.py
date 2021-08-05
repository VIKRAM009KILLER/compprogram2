# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.
def Rotate(a):
	new = []
	for i in a:
		new.append(i)
	x = new.pop(0)
	new.append(x)
	res = ''.join(new)

	return res

def isrotated(str1, str2):
	#Your code goes here
	new = []
	for i in str1:
		new.append(i)
	count = 0
	while(count <= len(new)):
		x = Rotate(str1)
		count += 1
		if x == str2:
			return True
		str1 = x

	return False



	pass