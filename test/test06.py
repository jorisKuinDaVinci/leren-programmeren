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
geraden = '_' * len(woord_te_raden)


# max 10 fouten
# tikt iemand de 'p' dan: print('_pp__')
while teller_fout < 10:
    geraden_letter = get_letter()
    print(geraden_letter)
    # stap 1: check of de letter in het woord voorkomt
    if geraden_letter in woord_te_raden:
        print(f'Goed geraden: {geraden_letter}')
        # stap 2: vervang de '_' door de letter
        for i in range(len(woord_te_raden)):
            if woord_te_raden[i] == geraden_letter:
                geraden = geraden[:i] + geraden_letter + geraden[i+1:]
        print(geraden)
        # stap 3: check of het woord geraden is
        if geraden == woord_te_raden:
            print(f'je hebt het woord geraden: {woord_te_raden}')
            break
    else:
        # stap 4: verhoog de teller
        teller_fout += 1
        # stap 5: print de fout geraden letters
        print(f'Fout geraden: {geraden_letter}')
        # stap 6: print het aantal pogingen dat je nog hebt
        fout_geraden.append(geraden_letter)
        print(f'Fout geraden: {fout_geraden}')
        print(f'Je hebt nog {10 - teller_fout} pogingen over')
        print(geraden)
else:
    # stap 7: print het woord als je het niet geraden hebt
    print(f'je hebt het niet geraden.\nHet woord was: {woord_te_raden}')    