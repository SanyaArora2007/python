import math

def interior_angles( sides ):
	return ( ( sides - 2  ) * 180  ) / sides

def exterior_angles( sides ):
	return 180 - interior_angles( sides )

def area_triangle( b, h ):
	return ( b * h ) / 2.0

def hypotenuse( a, b ):
	return math.sqrt( ( a ** 2 ) + ( b ** 2 ) )

def pie_chart( data ):
	total = 0.0
	p = 0
	while p < len( data ):
		total = total + data[p]
		p = p + 1

	p = 0
	degrees = []
	while p < len( data ):
		calculation = ( data[p] / total ) * 360.0
		degrees.append( calculation )
		p = p + 1
	return degrees


print( 'The angles of all the slices are ' + str( pie_chart( [ 12, 6, 9, 7, 2 ] ) ) )

print( 'The hypotenuse of a triangle with sides 3 and 5 is ' + str( hypotenuse( 3, 5 ) ) )

print( 'The are of a triangle with a height of 2, and base of 10 is ' + str( area_triangle( 10, 2) ) )

print( 'The exterior angles of a polygon with 3 side is ' + str( exterior_angles( 3 ) ) )

print( 'The interior angles of a polygon with 3 side is ' + str( interior_angles( 3 ) ) )