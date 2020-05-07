questions = [
	{ 'question': 'What is the capital of Switzerland', 'answer': 'Bern' },
	{ 'question': 'What is the world''s smallest country', 'answer': 'Vatican City' },
	{ 'question': 'Which river is the longest in the world', 'answer': 'Nile' },
	{ 'question': 'How many languages do they speak in Luxembourg', 'answer': '3' },
	{ 'question': 'Who is the author of the book Maze Runner', 'answer': 'James Dashner' },
	{ 'question': 'What is the largest dam in the world', 'answer': 'Three Gorges dam' },
	{ 'question': 'What is the official nickname for Texas', 'answer': 'Lone star state' },
	{ 'question': 'How many Earths could fit inside the sun', 'answer': '1.3 million' },
	{ 'question': 'Which counrty has the oldest continuously used national flag', 'answer': 'Denmark' },
	{ 'question': 'What is the capital of New Zealand', 'answer': 'Wellington' },
	{ 'question': 'How many hearts does an octopus have', 'answer': '3' },
	{ 'question': 'Which country produces the most coffee in the world', 'answer': 'Brazil'},
	{ 'question': 'How many times does the heart beat per day', 'answer': '100,000' },
]


score = 0
name = raw_input( 'enter your name : ' )
print( 'hello ' + name )
print( 'this is a question and answer game, have fun!' )
start = raw_input( 'are you ready (y/n) : ' )
if start == 'n':
	print( 'thats too sad, you missed a fun game' )
elif start == 'y':
	i = 0
	while i < len( questions ):

		chances = 3
		correct = False
		while chances > 0 and not correct:
			user_answer = raw_input( questions[ i ][ 'question' ] + '? ' )
			if user_answer.upper() == questions[ i ][ 'answer' ].upper():
				print( 'good job!' )
				correct = True
				score = score + 1
			else:
				print( 'wrong' )
				chances = chances - 1


		i = i + 1
	print( 'your score is ' + str( score ) )
	if score < len( questions ) /2:
		print( 'you can do better than that, come on' )
	elif score == len( questions ):
		print( 'amazing, 100%, can''t beat that' )
	else:
		print( ' you got over 50%' )