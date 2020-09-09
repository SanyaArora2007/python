import turtle as t
from random import random

def dice_outline( x1, y1, x2, y2, x3, y3, x4, y4, size):
	t.pencolor( '#000000' )
	t.pensize(size)
	t.goto( x1, y1 )
	t.pendown()
	t.goto( x2, y2 )
	t.goto( x3, y3 )
	t.goto( x4, y4 )
	t.goto( x1, y1 )


def dot( x, y ):
	t.penup()
	t.goto( x, y )
	t.pendown()
	t.begin_fill()
	t.color( 'black', 'black' )
	t.circle( 50 )
	t.end_fill()


def display_dice( number ):
	dice_outline( -300, -300, -300, 300, 300, 300, 300, -300, 10 )
	if number == 1:
		dot( 0, -50 )
	elif number == 2:
		dot( 0, 100 )
		dot( 0, -150 )
	elif number == 3:
		dot( -150, -200 )
		dot( 0, -50 )
		dot( 150, 100 )
	elif number == 4:
		dot( -150, 100 )
		dot( 150, 100 )
		dot( -150, -200 )
		dot(  150, -200 )
	elif number == 5:
		dot( 0, -50)
		dot( -150, 100 )
		dot( -150, -200 )
		dot( 150, 100 )
		dot( 150, -200 )
	elif number == 6:
		dot( 150, 100 )
		dot( -150, 100 )
		dot( -150, -50 )
		dot( 150, -50 )
		dot( -150, -200 )
		dot( 150, -200 )

def creates_range_and_display_dice( x, y ):
	t.reset()
	t.speed(0)
	t.penup()
	t.hideturtle()
	display_dice( int( random() * 6 + 1 ) )

s = t.getscreen()
s.onclick( creates_range_and_display_dice )

t.done()
