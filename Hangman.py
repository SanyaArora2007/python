from random import random

MOVIE_NAMES = [
	'frosty the snowman',
	'rudolph the red nose reindeer',
	'jingle bell rock',
	'its beginning to look a lot like christmas',
	'all i want for christmas is you',
	'silent night',
	'jingle bells',
	'winter wonderland',
	'let it snow',
]

HANGMANPICS = ['',
'''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def draw_hagman( lives ):
	print( HANGMANPICS[ 7 - lives ] )


def print_guessed( guessed ):
	output = ''
	p = 0
	while p < len( guessed ):
		output = output + guessed[p]
		p = p + 1
	print( output )


def first_guess( movie ):
	guessed = []
	position = 0
	while position < len( movie ):
		if movie[position] == ' ':
			guessed.append( ' ' )
		else:
			guessed.append( '_' )
		position = position + 1
	return guessed


number = int(random() * 100 ) % len( MOVIE_NAMES )
movie = MOVIE_NAMES[number]
guess = first_guess( movie )
lives = 7
already = set()


while lives > 0 and '_' in guess:
	draw_hagman( lives )
	print_guessed( guess )
	guessed_letter = raw_input( 'Pick a letter : ' )

	if guessed_letter in already:
		continue

	already.add( guessed_letter )

	p = 0
	found = False
	while p < len( movie ):
		if guessed_letter == movie[p]:
			guess[p] = guessed_letter
			found = True
		p = p + 1

	if not found:
		lives = lives - 1

print_guessed( guess )

if '_' in guess:
	draw_hagman( lives )
	print( 'You lost all your lives, Boo' )
else:
	print( 'Congrats, you completed the hangman' )