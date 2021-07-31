# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.



def fun_carrylessadd(x, y):

    str1 = ""
    while(x != 0):
        if y != 0:
            dx = x % 10
            dy = y % 10
            m = dx+dy
            if m >= 10:
                m = m-10
            str1 += str(m)
            x = x // 10
            y = y // 10
            # print(str1)
            
        else:
            m = x
            str1 += str(m)
            break
            # print(str1)
            
    return int(str1[::-1])	

			
				

	

