import string
# goede letters of niet? mini galgje!
# max 10 fouten
# tikt iemand de 'p' dan: print('_pp__')

def get_letter() -> str:
    while True:
        letter = input('Voer een letter in: ')
        if len(letter) != 1:
            print('Voer 1 (één) letter in!')
        elif letter not in string.ascii_lowercase:
            print('je voert geen letters in!')
        else:
            return letter
    
woord_te_raden = 'appel' 
teller_fout = 0   
fout_geraden = []
geraden = '_' * len(woord_te_raden)

while teller_fout < 10:
    geraden_letter = get_letter()
    print(geraden_letter)

print(f'je hebt het niet geraden.\nHet woord was: {woord_te_raden}')    