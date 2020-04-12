import random
      
'''    
My ID checker function wasn't sufficient and tbh I'm bored with this project
so I found another function at Github which is more pythonic.
My ID generating function is working fine and fast and it's the only example in this category ;)
 
'''


def idc(code):
    # credits goes to: https://github.com/RezaOptic/irvalidator-python/blob/develop/irvalidator/nationalid.py
    code = "0" * (len(code) - 10) + code
    code = list(map(int, code[::-1]))
    temp = 0
    for index, digit in enumerate(code[1:]):
        temp += digit * (index+2)
        
    r = divmod(temp, 11)[1]
    if r < 2 and r == code[0]:
        return True
    elif r >= 2 and (11 - r) == code[0]:
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
