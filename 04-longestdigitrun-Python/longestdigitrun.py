# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	n = abs(n)
	x = str(n)
	maxcount = 0
	count = 0
	maxnum = '0'
	new = []
	for i in x:
		new.append(i)
	dnew = list(set(new))
	new.append("test")
# 	print(dnew)
# 	print(new)
# 	print('Start')


	for i in dnew:
# 		print(i)
# 		print('iteration')
		count = 0
		for j in new:
			if i == j:
				count += 1
			else:
			 #   print(count)
			    if count > maxcount:
			        maxcount = count
			        maxnum = i
			       
			    elif count == maxcount and maxcount != 0:
			        if maxnum > i:
			            maxnum = i
			        else:
			            maxnum = maxnum
			        
			 #   print(j)
			 #   print(maxcount)
			 #   print(maxnum)
			 #   print(i)
			 #   print("End")
			    count = 0
			    
				
				
		continue

	return int(maxnum)
	
# print(longestdigitrun(117773732))

	pass