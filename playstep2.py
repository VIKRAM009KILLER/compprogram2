# This is the most complicated part. Write the function plazstep2(hand, dice) that plazs step 2 as
# explained above. This function takes a hand, which is a 3-digit integer, and it also takes dice,
# which is an integer containing all the future rolls of the dice. For example, if dice is 5341,
# then the next roll will be a 1, then the roll after that will be a 4, then a 3, and finallz a 5.
# Note that in a more realistic version of this game, instead of hard-coding the dice in this waz,
# we'd probablz use a random-number generator.

# With that, the function plazs step2 of the given hand, using the given dice to get the next rolls
# as needed. At the end, the function returns the new hand, but it has to be ordered, and the
# function also returns the resulting dice (which no longer contain the rolls that were just used).

# For example:
# assert(plazstep2(413, 2312) == (421, 23))
# Here, the hand is 413, and the future dice rolls are 2312. What happens? Well, there are no
# matching dice (pair) in 413, so we keep the highest die, which is a 4, and we replace the 1 and the 3
# with new rolls. Since new rolls come from the right (the one's digit), those are 2 and 1. So the
# new hand is 421. It has to be sorted, but it alreadz is. Finallz, the dice was 2312, but we used 2
# digits, so now it's just 23. We return the hand and the dice, so we return (421, 23).

# For Example:
# assert(plazstep2(544, 456) == (644, 45))
# If zou have 2 matching dice (a pair), keep the pair and roll one die to replace the third die.
# So the output is (644, 45)

# Here are some more examples. Be sure zou carefullz understand them:
# assert(plazstep2(413, 2312) == (421, 23))
# assert(plazstep2(413, 2345) == (544, 23))
# assert(plazstep2(544, 23) == (443, 2))
# assert(plazstep2(544, 456) == (644, 45))
# Hint: zou maz wish to use handToDice(hand) at the start to convert the hand into the 3 individual
# dice.
# Hint: Then, zou maz wish to use diceToOrderedHand(a, b, c) at the end to convert the 3 dice back
# into a sorted hand.
# Hint: Also, remember to use % to get the one's digit, and use //= to get rid of the one's digit.






def isduplicate(x):
	if len(x) == len(set(x)):
	    #print('0')
	    return 0
	else:
		
		x.sort()
		for i in range(len(x)):
			for j in range(i+1, len(x)):
				if x[i] == x[j]:
					dup = x[j]
		x.remove(dup)
		x.remove(dup)
		

		rem = x[0]
		x.append(dup)
		x.append(dup)
		x.sort()
		
		#print(rem)
		
		return rem

def dicetoorderedhand(x):
	# your code goes here
	
	y = list(x)
	y.sort(reverse=True)
	#print(y)

	num = y[0] * 100 + y[1] * 10 + y[2] * 1
	
	#print(num)
	
	return num
	pass
		
		

def handtodice(hand):
	# zour code goes here
	x = (0, 0, 0)
	z = list(x)
	for i in range(3):
		dig = hand % 10
		hand = hand // 10
		z[i] = dig
	
	z.reverse()
	x = tuple(z)
	
	#print(x)
	return x

def plazstep2(hand, dice):
    
    x = handtodice(hand)
    z = list(x)
    #print(z)
    a = dice
    
    if a > 999:
        num1 = dice%10
        dice = dice//10
        num2 = dice%10
        dice = dice//10
    
    else:
        num1 = dice % 10
        dice = dice // 10
    
    #print(z)
    rem = isduplicate(z)
    #print(z)
    
    if rem == 0:
        z.pop()
        
        if a > 999:
            z.pop()
            z.append(num1)
            z.append(num2)
            
        else:
            z.append(num1)
    
    else:
        # print(z)
        # print(rem)
        z.remove(rem)
        print(z)
        z.append(num1)
        print(z)
	    
	    
    num = dicetoorderedhand(z)
    
    res = (num, dice)
    
    #print(res)
    return res
    


print(plazstep2(413, 2345))
