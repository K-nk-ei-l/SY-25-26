print('What is your star sign?')
star_sign = input('Enter your star sign: ')
if star_sign.lower() == 'aries':
    print('♈︎')
elif star_sign.lower() == 'taurus':
    print('♉︎')
elif star_sign.lower() == 'gemini':
    print('♊︎')
elif star_sign.lower() == 'cancer':
    print('♋︎')
elif star_sign.lower() == 'leo':
    print('♌︎')
elif star_sign.lower() == 'virgo':
    print('♍︎')
elif star_sign.lower() == 'libra':
    print('♎︎')
elif star_sign.lower() == 'scorpio':
    print('♏︎')
elif star_sign.lower() == 'sagittarius':
    print('𓀎')
elif star_sign.lower() == 'capricorn':
    print('♑︎')
elif star_sign.lower() == 'aquarius':
    print('♒︎')
elif star_sign.lower() == 'pisces':
    print('♓︎')
else:

    print('Star sign not recognized. Please try again.')
    
    
    star_sign = input('Please try again: ')

if star_sign.lower() == 'again':
    print('Very very funny, but no, please enter a star sign.')

star_sign = input('Please enter a star sign: ')

if star_sign.lower() == 'a star sign':
    print('You are pissing me off. Type a sign')

star_sign = input('Please enter a star sign: ')

if star_sign.lower() == 'a sign':
    raise Exception('Application crashed intentionally!')