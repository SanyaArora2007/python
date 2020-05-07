from random import random

MOVIE_NAMES = [
	'the maze runner',
	'pearl harbor',
	'my girl',
	'the scorch trial',
	'the death cure',
	'wreck it ralph',
	'spider man far from home'
	'avengers end game',
	'avengers infinity war',
	'harry potter and the chamber of secrets',
	'trolls',
	'jumanji',
	'skyfal',
	'casino royal',
	'parasite',
	'star wars',
	'onword',
	'frozen',
	'knives out',
	'aqua man',
	'captain marvel',
	'fast and furious',
	'it',
	'black panther',
	'jojo rabbit',
	'stranger things',
	'office',
	'friends',
]

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
	print( 'You have ' + str( lives ) + ' lives' )
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
	print( 'You lost all your lives, Boo' )
else:
	print( 'Congrats, you completed the hangman' )