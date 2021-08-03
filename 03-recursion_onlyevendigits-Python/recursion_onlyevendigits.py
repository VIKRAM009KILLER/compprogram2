# Without using iteration and without using strings, 
# write the recursive function onlyEvenDigits(L), 
# that takes a list L of non-negative integers 
# (you may assume that), and returns a new list of 
# the same numbers only without their odd digits 
# (if that leaves no digits, then replace the number with 0). 
# So: onlyEvenDigits([43, 23265, 17, 58344]) returns [4, 226, 0, 844]. 
# Also the function returns the empty list if the original list is empty. 
# Remember to not use strings. You may not use loops/iteration in this problem.
def removeodd(n, s):
    if n == 0:
        return 0
    num = n % 10

    # print(n)
    
        
    n = n // 10
    if num % 2 == 0:
            
        c = s - len(str(n))
        if n == 0:
            c = s
        
        # print(len(str(n)))
        # print(s)
        # print(c-1)
        return num * 10**(c-1) + removeodd(n, s)
    else:
        
        
        s = s - 1
        # print(s)
        return 0 + removeodd(n, s)

def fun_recursion_onlyevendigits(l):
	if len(l) == 0:
		return []
	num = l.pop(0)
	newnum = removeodd(num, len(str(num)))
		

	

	return [newnum] + fun_recursion_onlyevendigits(l)
		