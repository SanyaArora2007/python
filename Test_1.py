def count_letter( name, letter ):
	p = 0
	count = 0
	while p < len( name ):
		if name[p] == letter :
			count = count + 1
		p = p + 1
	return count

print( count_letter( 'mississippi', 's' ) )
print( count_letter( 'mississippi', 'i' ) )
print( count_letter( 'mississippi', 'p' ) )