# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine 
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and 
# diagonally.

def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	x1 = qR
	y1 = qC
	x2 = oR
	y2 = oC

	if x1 == x2:
		return True
	if y1 == y2:
		return True
	if abs(x1-x2) == abs(y1-y2):
		return True
	else:
		return False

	
	
	
	pass