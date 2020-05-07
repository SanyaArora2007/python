numbers = [ 7, 9, 14, 10, 8, 23, 71, 36, 102 ]
n = 0
divisible_3 = []
while n < len( numbers ):
	if numbers[n] % 3 == 0:
		divisible_3.append( numbers[n] )
	n = n + 1
print( divisible_3 )