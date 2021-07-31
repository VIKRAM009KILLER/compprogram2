# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.



def fun_carrylessadd(x, y):

    newnum = []
    while(x != 0):
        if y != 0:
            dx = x % 10
            dy = y % 10
            m = dx+dy
            if m >= 10:
                m = m-10
            newnum.append(m)
            x = x // 10
            y = y // 10
        else:
            continue
    number = 0
    for i in range(len(newnum)):
        d = newnum[i] * 10**i
        number += d
    return number		

			
				

	

