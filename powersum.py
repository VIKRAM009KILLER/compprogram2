# powerSum(n, k) [15 pts]
# Write the function powerSum(n, k) that takes two 
# possibly-negative integers n and k and returns the 
# so-called power sum: Specify the time complexity based 
# on the solution that you have given. [Hint: This can be 
# solved in (n * log k)  or better.

#    1**k + 2**k + ... + n**k

# If n is negative, return 0. Similarly, if k is negative, 
# return 0.

def powerSum(n, k):
    # Your code goes here...
    if n <= 0 or k < 0:
        return 0
    sum = 0
    for i in range(1, n+1):
        sum += i ** k

    return sum

# Write your own test cases here...
count = 0

if(powerSum(4, 5) == 1300):
    count += 1
if(powerSum(4, 2) == 30):
    count += 1
if(powerSum(9, 3) == 2025):
    count += 1
if(powerSum(0, 3) == 0):
    count += 1
if(powerSum(9, 0) == 9):
    count += 1
if(powerSum(0, 0) == 0):
    count += 1



if count == 6:
    print ("All test cases passed...")
else:
    print("%d testcases passed, %s failed" %(count, 6-count))