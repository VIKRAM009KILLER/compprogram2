# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def isKarpekar(n):
    num = n ** 2
    if num < 10:
        return False
    # print(num)
    x = str(num)
    # print(x)
    
    
    a = len(x) // 2
    while(a >= 1):
         n1 = int(x[:a])
         n2 = int(x[a:])
         if n1 == 0 or n2 == 0:
             return False
         newnum = n1 + n2
         if newnum == n:
             return True
         a -= 1
             
    return False
           
        
def fun_nth_kaprekarnumber(n):
    if n == 0:
        return 1
    # if n == 1:
    #     return 9

    count = 0
    m = 10 ** 50
    for i in range(2, m):
        if(isKarpekar(i)):
            print(i)
            count += 1
        if count == n:
            return i