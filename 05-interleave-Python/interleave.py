# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	new = ''
	count = 0
	d = abs(len(s1) - len(s2))

	for i, j in zip(s1, s2):
		new += i
		new += j
		


	
	if len(s1) == len(s2):
		return new
	if len(s1) > len(s2):
		res = s1[-d:]
		new += res
		return new
	if len(s1) < len(s2):
		res = s2[-d:]
		new += res
		return new
		