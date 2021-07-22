# Write the function nearestBusStop(street) that takes a 
# non-negative int street number, and returns the nearest 
# bus stop to the given street, where buses stop every 8th street, 
# including street 0, and ties go to the lower street, 
# so the nearest bus stop to 12th street is 8th street, 
# and the nearest bus stop to 13 street is 16th street.



def fun_nearestbusstop(street):
	n = street
	if n <= 4:
		return 0
	
	m = street // 8 + 1
	
	stoplow = 8 * m - 8
	stoptop = 8 * m 

	dlow = street - stoplow
	dtop = stoptop - street

	if dlow <= dtop:
		res = stoplow
	else:
		res = stoptop



	
	

	return res
