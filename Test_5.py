numbers = [ 56, 78, 34, 23, 21 ]

def square( numbers ):
	p = 0
	squares = []
	while p < len( numbers ):
		answer = numbers[p] * numbers[p]
		squares.append( answer )
		p = p + 1
	return squares

print( square( numbers ) )