def compound_interest( i, p, y ):
	final = ( i * ( ( 100 + p ) / 100.0 ) ** y )
	return final

interest = float( raw_input( 'How much money are you investing : ' ) )
percentage_rate = float( raw_input( 'By what percentage is the money increasing : ' ) )
years = float( raw_input( 'How many years : ' ) )

calculated = compound_interest( interest, percentage_rate, years )
print( 'The amount of money that you will have after ' + str( years ) + ' years is ' + str( calculated ) )