import turtle as t
#t.hideturtle()

def circle( x, y, fill, radius ):
	t.penup()
	t.goto( x, y )
	t.setheading( 0 )
	t.pendown()
	t.color( 'black', fill )
	t.begin_fill()
	t.circle( radius )
	t.end_fill()

def arm( x, y, direction ):
	t.penup()
	t.goto( x, y )
	t.pendown()
	if direction == 'left':
		t.forward(60)
		t.left(45)
	else:
		t.back(60)
		t.left(135)

	t.forward(40)
	t.back(40)

	if direction == 'left':
		t.right(45)
	else:
		t.left(45)

	t.forward(40)
	t.back(40)

	if direction == 'left':
		t.right(45)
	else:
		t.left(45)

	t.forward(40)
	t.back(40)

	if direction == 'left':
		t.left(45)
	else:
		t.left(135)

t.speed(10)
circle( 0, -270, 'dark grey', 120 )
circle( 0, -30, 'light grey', 90 )
circle( 0, 150, 'light blue', 75 )

arm( 90, 60, 'left' )
arm( -90, 60, 'right' )

circle( 0, 100, 'red', 10 )
circle( 0, 60, 'red', 10 )
circle( 0, 20, 'red', 10)
circle( 0, -60, 'red', 10 )
circle( 0, -100, 'red', 10 )
circle( 0, -140, 'red', 10 )
circle( -25, 250, 'blue', 5)
circle( 25, 250, 'blue', 5)


t.penup()
t.goto( 0, 250 )
t.setheading(240)
t.pendown()
t.color( 'orange', 'orange' )
t.begin_fill()
t.forward(40)
t.setheading(0)
t.forward(40)
t.setheading(120)
t.forward(40)
t.end_fill()
t.hideturtle()

t.done()