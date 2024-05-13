import string
# goede letters of niet? mini galgje!

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
geraden = list('_' * 5)


# max 10 fouten
# tikt iemand de 'p' dan: print('_pp__')
while teller_fout < 10:
    geraden_letter = get_letter()
    print(geraden_letter)
else:
    #print het woord als je het niet geraden hebt
    print(f'je hebt het niet geraden.\nHet woord was: {woord_te_raden}') 