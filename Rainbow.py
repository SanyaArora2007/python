import turtle as t

t.speed(10)
t.penup()
t.hideturtle()

def strips( x, y, size, r, color ):
	t.pencolor(color)
	t.pensize(size)
	t.left(90)
	t.goto( x, y )
	t.pendown()
	t.circle( r, 180 )
	t.penup()
	t.left(90)

strips( 100, -350, 50, 75, '#9400D3' )
strips( 150, -350, 50, 125, '#4B0082' )
strips( 200, -350, 50, 175, '#0000FF' )
strips( 250, -350, 50, 225, '#00FF00' )
strips( 300, -350, 50, 275, '#FFFF00' )
strips( 350, -350, 50, 325, '#FF7F00' )
strips( 400, -350, 50, 375, '#FF0000' )
 

t.done()