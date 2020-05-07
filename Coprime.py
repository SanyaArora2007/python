def find_factors( number ):
    factors = set()
    factors.add( 1 )
    factors.add( number )
    check = 2
    while check <= number/2:
        if number % check == 0:
            factors.add( check )
        check = check + 1
    return factors

def prime( number ):
    factors = find_factors( number )
    if len( factors ) == 2:
        return str( number ) + " is Prime"
    else:
        return str( number ) + " is a Consonant" 

def gcf( x, y, z ):
    fx = find_factors( x )
    fy = find_factors( y )
    fz = find_factors( z )
    cf = fx.intersection( fy, fz )
    return max( cf )


def print_gcf( a, b, c ):
    print( 'the greatest common factor of ' + str( a ) + str( b ) + ' and ' + str( c ) +  'is ' )

def coprime( c, d, e ):
    stored = gcf( c, d, e )
    if stored == 1:
        return True
    else:
        return False

def print_coprime( e, f, g ):
    is_coprime = coprime( e, f, g )
    if is_coprime:
        print( str( e ) + ' and ' + str( f ) + ' and ' + str( g ) + ' are coprime' )
    else:
        print( str( e ) + ' and ' + str( f ) + ' and ' + str( g ) + ' are not coprime' )
        
print_coprime( 1, 2, 3 )