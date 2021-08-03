# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46
def isTidy(n):
    num = str(n)
    oldlist = []
    for i in num:
        oldlist.append(i)
    
    oldlist.sort()
    res = ''
    finnum = res.join(oldlist)
    if finnum == num:
        return True
    else:
        return False
    


def fun_nth_tidynumber(n):
    if n <= 8:
        return n+1
    m = 10**50
    count = 8
    for i in range(11, m):
        if(isTidy(i)):
            count += 1
        if count == n:
            return i

    return 0