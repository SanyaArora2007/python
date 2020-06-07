import turtle as t

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

def drawX_00( color = 'red' ):
	line( -100, 100, -300, 300, color )
	line( -300, 100, -100, 300, color )

def drawX_01( color = 'red' ):
	line( -100, 100, 100, 300, color )
	line( 100, 100, -100, 300, color )

def drawX_02( color = 'red' ):
	line( 100, 100, 300, 300, color )
	line( 300, 100, 100, 300, color )

def drawX_10( color = 'red' ):
	line( -300, -100, -100, 100, color )
	line( -300, 100, -100, -100, color )

def drawX_11( color = 'red' ):
	line( -100, -100, 100, 100, color )
	line( -100, 100, 100, -100, color )

def drawX_12( color = 'red' ):
	line( 100, -100, 300, 100, color )
	line( 300, -100, 100, 100, color )

def drawX_20( color = 'red' ):
	line( -100, -300, -300, -100, color )
	line( -100, -100, -300, -300, color )

def drawX_21( color = 'red' ):
	line( -100, -300, 100, -100, color )
	line( -100, -100, 100, -300, color )

def drawX_22( color = 'red' ):
	line( 100, -300, 300, -100, color )
	line( 100, -100, 300, -300, color )


def drawO_00( color = 'blue' ):
	circle( -200, 100, color )

def drawO_01( color = 'blue' ):
	circle( 0, 100, color )

def drawO_02( color = 'blue' ):
	circle( 200, 100, color )

def drawO_10( color = 'blue' ):
	circle( -200, -100, color )

def drawO_11( color = 'blue' ):
	circle( 0, -100 , color )

def drawO_12( color = 'blue' ):
	circle( 200, -100 , color )

def drawO_20( color = 'blue' ):
	circle( -200, -300, color )

def drawO_21( color = 'blue' ):
	circle( 0, -300, color )

def drawO_22( color = 'blue' ):
	circle( 200, -300, color )

def show( x, y ):
	if x > -100 and x < 100 and y < 100 and y > -100:
		drawX_11()
	elif x > -300 and x < -100 and y > 100 and y < 300:
		drawX_00()
	elif x > -100 and x < 100 and y > 100 and y < 300:
		drawX_01()
	elif x > 100 and x < 300 and y > 100 and y < 300:
		drawX_02()
	elif x > 100 and x < 300 and y > -100 and y < 300:
		drawX_12()
	elif x > -300 and x < -100 and y > -10 0 and y < 100:
		drawX_10()
	elif x > -300 and x < -100 and y > -300 and y < 100:
		drawX_20()
	elif x > -100 and x < 100 and y > -300 and y < -100:
		drawX_21()
	elif x > 100 and x < 300 and y > -300 and y < -100:
		drawX_22()

s = t.getscreen()
s.onclick(show)
t.speed(0)
t.hideturtle()

grid()

t.done()