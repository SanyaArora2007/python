import turtle as t
turn = 0
moves = [ [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '] ]

def line( x1, y1, x2, y2, color = 'black', size = 1):
	t.penup()	
	t.goto( x1, y1 )
	t.pensize( size )
	t.pendown()
	t.color( color )
	t.goto( x2, y2 )

def circle( x1, y1, color = 'blue', size = 1 ):
	t.penup()
	t.goto( x1, y1 )
	t.pensize( size )
	t.pendown()
	t.color( color )
	t.circle( 100 )

def grid():
	line( -300, 100, 300, 100, 'black', 6 )
	line( -300, -100, 300, -100, 'black', 6 )
	line( -100, -300, -100, 300, 'black', 6 )
	line( 100, -300, 100, 300, 'black', 6 )

def drawX( i, j, color = 'red' ):
	line( -100 + i * 200, 100 - j * 200, -300 + i * 200, 300 - j * 200, color )
	line( -300 + i * 200, 100 - j * 200, -100 + i * 200, 300 - j * 200, color )

def drawO( i, j, color = 'blue' ):
	circle( -200 + i * 200, 100 - j * 200, color )

def show( x, y ):
	global turn
	global moves

	if x > -100 and x < 100 and y < 100 and y > -100:
		i = 1
		j = 1
	elif x > -300 and x < -100 and y > 100 and y < 300:
		i = 0
		j = 0
	elif x > -100 and x < 100 and y > 100 and y < 300:
		i = 1
		j = 0
	elif x > 100 and x < 300 and y > 100 and y < 300:
		i = 2
		j = 0
	elif x > 100 and x < 300 and y > -100 and y < 300:
		i = 2
		j = 1
	elif x > -300 and x < -100 and y > -100 and y < 100:
		i = 0
		j = 1
	elif x > -300 and x < -100 and y > -300 and y < 100:
		i = 0
		j = 2
	elif x > -100 and x < 100 and y > -300 and y < -100:
		i = 1
		j = 2
	elif x > 100 and x < 300 and y > -300 and y < -100:
		i = 2
		j = 2

	if moves[ i ][ j ] == ' ':
		turn = turn + 1
		if turn % 2 == 1:
			drawO( i, j )
			moves[ i ][ j ] = 'O'
		else:
			drawX( i, j )
			moves[ i ][ j ] = 'X'
		find_winner()

def find_winner():
	global moves

	if moves[ 0 ][ 0 ] == moves[ 1 ][ 0 ] and moves[ 1 ][ 0 ] == moves[ 2 ][ 0 ] and moves[ 0 ][ 0 ] != ' ':
		line( -300, 200, 300, 200, 'green', 3 )
		return moves[ 0 ][ 0 ]

	elif moves[ 0 ][ 1 ] == moves[ 1 ][ 1 ] and moves[ 1 ][ 1 ] == moves[ 2 ][ 1 ] and moves[ 0 ][ 1 ] != ' ':
		line( -300, 0, 300, 0, 'green', 3 )
		return moves[ 0 ][ 1 ]

	elif moves[ 0 ][ 2 ] == moves[ 1 ][ 2 ] and moves[ 1 ][ 2 ] == moves[ 2 ][ 2 ] and moves[ 0 ][ 2 ] != ' ':
		line( -300, -200, 300, -200, 'green', 3 )
		return moves[ 2 ][ 0 ]

	elif moves[ 0 ][ 0 ] == moves[ 1 ][ 0 ] and moves[ 1 ][ 0 ] == moves[ 2 ][ 0 ] and moves[ 0 ][ 0 ] != ' ':
		line( -200, 300, -200, -300, 'green', 3 )
		return moves [ 0 ][ 0 ]

	elif moves[ 1 ][ 0 ] == moves[ 1 ][ 1 ] and moves[ 1 ][ 1 ] == moves[ 1 ][ 2 ] and moves[ 1 ][ 0 ] != ' ':
		line( 0, 300, 0, -300, 'green', 3 )
		return moves[ 1 ][ 0 ]

	elif moves[ 2 ][ 0 ] == moves[ 2 ][ 1 ] and moves[ 2 ][ 1 ] == moves[ 2 ][ 2 ] and moves[ 2 ][ 0 ] != ' ':
		line( 200, 300, 200, -300, 'green', 3 )
		return moves[ 2 ][ 0 ]

	elif moves[ 0 ][ 0 ] == moves[ 1 ][ 1 ] and moves[ 1 ][ 1 ] == moves[ 2 ][ 1 ] and moves[ 0 ][ 0 ] != ' ':
		line( -300, 300, 300, -300, 'green', 3 ) 
		return moves[ 0 ][ 0 ]

	elif moves[ 2 ][ 0 ] == moves[ 1 ][ 1 ] and moves[ 1 ][ 1 ] == moves[ 0 ][ 2 ] and moves[ 2 ][ 0 ] != ' ':
		line( 300, 300, -300, -300, 'green', 3 )
		return moves[ 2 ][ 0 ]

	return ' '


find_winner()
s = t.getscreen()
s.onclick(show)
t.speed(0)
t.hideturtle()

grid()

t.done()