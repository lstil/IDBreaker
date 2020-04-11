def idc(code):
    try:
        code = int( code )
    except:
        return False

    range_id = range( 1, 733 )
    str_code = str( code )
    
    if len( str_code ) == 8:
        str_code = '0' * 2 + str_code
    if len( str_code ) == 9:
        str_code = '0' + str_code
    if int( str_code[ 0 ] ) == 0 and int( str_code[ 1 ] ) == 0:
        _part_id = str_code[ 2 ]
    elif int( str_code[ 0 ] ) == 0:
        _part_id = str_code[ 1 ] + str_code[ 2 ]
    elif len( str_code ) == 10:
        _part_id = str_code[ 0 ] + str_code[ 1 ] + str_code[ 2 ]

    if len( str_code ) == 10 and int( _part_id ) in range_id:
        to_tal = 0
        for x in range( 1, 10 ):
            s_ad = int( str_code[ x - 1 ] ) * (11 - x)
            to_tal = to_tal + s_ad
        avr = to_tal % 11
        if int( avr ) < 2 and int( str_code[ 9 ] ) == int( avr ):
            return True
        elif int( avr ) >= 2:
            if (11 - int( avr )) == int( str_code[ 9 ] ):
                return True

    return False


def idg():
    first = random.randint( 1, 732)
    if len( str( first ) ) == 1: first = "0" * 2 + str( first )
    if len( str( first ) ) == 2: first = "0" + str( first )
    second = random.randint( 100000, 999999 )
    num = str( first ) + str( second )
    to_tal = 0
    for x in range( 1, 10 ):
        s_ad = int( num[ x - 1 ] ) * (11 - x)
        to_tal = to_tal + s_ad
    avr = to_tal % 11
    if int( avr ) < 2: num = num + str( avr )
    elif int( avr ) >= 2:
        fres = (11 - int( avr ))
        num = num + str( fres )
    return num
