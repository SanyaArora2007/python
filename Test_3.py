phrase = 'SuCHi is an amaZing mom'

def count_vowels( phrase ):
	p = 0
	count = 0
	while p < len( phrase ):
		if phrase[p] in 'aeiou':
			count = count + 1
		p = p + 1
	return count

print( count_vowels( phrase ) )

def capitalize( phrase ):
	output = ''
	p = 0
	while p < len( phrase ):
		if phrase[p] == ' ':
			output = output + ' ' + phrase[p + 1].upper()
			p = p + 1
		elif p == 0:
			output = output + phrase[p].upper()
		else:
			output = output + phrase[p].lower()
		p = p + 1
	return output

print( capitalize( phrase ) ) 