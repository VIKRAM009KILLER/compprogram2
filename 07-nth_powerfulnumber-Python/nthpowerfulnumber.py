# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

def Seiv(n):
	if n <= 1:
	    return False
	for i in range(2, n):
	    if n % i == 0:
	        return False
	        
	return True
	


def Powernum(n):
    if n == 1:
        return True
    
    if n == 2 or n == 3:
        return False
    count = 0
    for i in range(2, n):
        if( n % i == 0):
            count += 1
            if(Seiv(i)):
                num = i ** 2
                if n % num != 0:
                    return False
            
                
        
    if count == 0:
        return False
    # print(count)
    return True

def nthpowerfulnumber(n):
	# Your code goes here
	if n == 0:
	    return 1
	count = 0
	m = 10 ** 6
	for i in range(2, m):

		if(Powernum(i)):
		    
		    count += 1

		if count == n:
			return i
