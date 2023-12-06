naam = input('wat is je naam?')
print('hallo ' + naam + ' je loopt door een bos. je bent verdwaald')
try:
    keuze_1 = input('je staat voor een splitsing, welke kant kiest je? (links of rechts)')
except:
    while True:
        try: 
            print("Dat is niet een keuze!(kies links of rechts!)")
            keuze_1 = input('je staat voor een splitsing, welke kant kiest je? (links of rechts)')
            break
        except:
            print("Dat is niet een keuze!(kies links of rechts!)")
if keuze_1 == 'links':
    print('je loopt verder en komt een beer tegen, je rent weg maar de beer rent achter je aan en eet je op')
    print('game over')
elif keuze_1 == 'rechts':
    print('je loopt verder en je komt aan bij een huis')
    try:
        keuze_2 = input('je kunt kiezen om aan te bellen of om weg te lopen, wat doe je? (aanbellen of weglopen)')
    except:
        while True:
            try: 
                print("Dat is niet een keuze!(kies aanbellen of weglopen!)")
                keuze_2 = input('je kunt kiezen om aan te bellen of om weg te lopen, wat doe je? (aanbellen of weglopen)')
                break
            except:
                print("Dat is niet een keuze!(kies aanbellen of weglopen!)")
    if keuze_2 == 'aanbellen':
        try:
            keuze_2_5 = input('er doet niemand open je ziet een apparraat aan het huis hangen, je moet een code invoeren. (code invoeren of weglopen)')
        except:
            while True:
                try: 
                    print("Dat is niet een keuze!(kies code invoeren of weglopen!)")
                    keuze_2_5 = input('er doet niemand open je ziet een apparraat aan het huis hangen, je moet een code invoeren. (code invoeren of weglopen)')
                    break
                except:
                    print("Dat is niet een keuze!(kies code invoeren of weglopen!)")
        if keuze_2_5 == 'code invoeren':
            print('je voert de code in')
            input('voer de code in: ')
            if input <= '1234':
                print('je hebt de code fout ingevoerd en het apparaat ontploft in je gezicht. je sterft.')
                print('game over')
            elif input >= '1234':
                print('je hebt de code fout ingevoerd en het apparaat ontploft in je gezicht. je sterft.')
                print('game over')
            elif input == '1234':
                print('je hebt de code goed ingevoerd en de deur gaat open.')
                try:
                    keuze_3 = input('er staat een oude vrouw in het huis, ze vraagt of je binnen wilt komen, wat doe je? (binnenkomen of weglopen)')
                except:
                    while True:
                        try:
                            print("Dat is niet een keuze!(kies binnenkomen of weglopen!)")
                            keuze_3 = input('er staat een oude vrouw in het huis, ze vraagt of je binnen wilt komen, wat doe je? (binnenkomen of weglopen)')
                            break
                        except:
                            print("Dat is niet een keuze!(kies binnenkomen of weglopen!)")
                if keuze_3 == 'binnenkomen':
                    print('je komt binnen en de vrouw vraagt of je wat wilt drinken.')
                    try:
                        keuze_4 = input('wil je drinken? (ja of nee)')
                    except:
                        while True:
                            try:
                                print("Dat is niet een keuze!(kies ja of nee!)")
                                keuze_4 = input('wil je drinken? (ja of nee)')
                                break
                            except:
                                print("Dat is niet een keuze!(kies ja of nee!)")
                    if keuze_4 == 'ja':
                        print('je zegt ja en de vrouw geeft je een drankje, je drinkt het op en sterft')
                        print('game over')
                    elif keuze_4 == 'nee':
                        print('je zegt nee en de vrouw wordt boos, ze pakt een mes en steekt je neer')
                        print('game over')
                elif keuze_3 == 'weglopen':
                    print('je loopt weg en een beer valt je aan. je sterft aan je verwondingen.')
                    print('game over')
        if keuze_2_5 == 'weglopen':
            print('je loopt weg en een beer valt je aan. je sterft aan je verwondingen.')
            print('game over')
    elif keuze_2 == 'weglopen':
        print('je loopt weg en komt aan bij een rivier')
        try:
            keuze_5 = input('er is een brug. je kunt kiezen om te zwemmen of om over de brug te lopen, wat doe je? (zwemmen of over de brug lopen)')
        except:
            while True:
                try:
                    print("Dat is niet een keuze!(kies zwemmen of over de brug lopen!)")
                    keuze_5 = input('er is een brug. je kunt kiezen om te zwemmen of om over de brug te lopen, wat doe je? (zwemmen of over de brug lopen)')
                    break
                except:
                    print("Dat is niet een keuze!(kies zwemmen of over de brug lopen!)")
        if keuze_5 == 'over de brug lopen':
            print('je loopt over de brug en de brug stort in, je valt in het water en verdrinkt')
            print('game over')
        elif keuze_5 == 'zwemmen':
            print('je gaat zwemmen en komt veilig aan de overkant.')
            print('je loopt verder en komt aan bij een weg')
            try:
                keuze_6 = input('je kunt kiezen om te oversteken of verder door het bos te lopen wat doe je? (oversteken of door het bos lopen)') 
            except:
                while True:
                    try:
                        print("Dat is niet een keuze!(kies oversteken of door het bos lopen!)")
                        keuze_6 = input('je kunt kiezen om te oversteken of verder door het bos te lopen wat doe je? (oversteken of door het bos lopen)')
                        break
                    except:
                        print("Dat is niet een keuze!(kies oversteken of door het bos lopen!)")
            if keuze_6 == 'oversteken':
                print('je steekt over en wordt aangereden door een auto')
                print('game over')
            elif keuze_6 == 'door het bos lopen':
                print('je loopt door het bos en komt aan bij een zebrapad')
                try:
                    keuze_7 = input('je kunt kiezen om over te steken of om te wachten wat doe je? (oversteken of wachten)')
                except:
                    while True:
                        try:
                            print("Dat is niet een keuze!(kies oversteken of wachten!)")
                            keuze_7 = input('je kunt kiezen om over te steken of om te wachten wat doe je? (oversteken of wachten)')
                            break
                        except:
                            print("Dat is niet een keuze!(kies oversteken of wachten!)")
                if keuze_7 == 'wachten':
                    print('je wacht en je wordt neergeschoten door een jager')
                    print('game over')
                elif keuze_7 == 'oversteken':
                    print('je steekt over en komt bij een ander bos.')
                    print('je loopt verder en komt aan bij een huis met een bordje "te koop"')
                    try:
                        keuze_8 = input('je kunt kiezen om het huis te kopen of om verder te lopen wat doe je? (huis kopen of verder lopen)')
                    except:
                        while True:
                            try:
                                print("Dat is niet een keuze!(kies huis kopen of verder lopen!)")
                                keuze_8 = input('je kunt kiezen om het huis te kopen of om verder te lopen wat doe je? (huis kopen of verder lopen)')
                                break
                            except:
                                print("Dat is niet een keuze!(kies huis kopen of verder lopen!)")
                    if keuze_8 == 'huis kopen':
                        print('je koopt het huis en gaat er wonen')
                        print('je woont er 10 jaar en je sterft door een ziekte. je ziet je familie en vrienden nooit meer en sterft alleen.')
                    elif keuze_8 == 'verder lopen':
                        print('je loopt verder en komt bij een kruispunt')
                        try:
                            keuze_9 = input('je kunt kiezen om links of rechts te gaan wat doe je? (links of rechts)')
                        except:
                            while True:
                                try:
                                    print("Dat is niet een keuze!(kies links of rechts!)")
                                    keuze_9 = input('je kunt kiezen om links of rechts te gaan wat doe je? (links of rechts)')
                                    break
                                except:
                                    print("Dat is niet een keuze!(kies links of rechts!)")
                        if keuze_9 == 'links':
                            print('je gaat links en ziet iets bekends')
                            try:
                                keuze_10 = input('je kunt kiezen om er naar toe te gaan of om verder te lopen wat doe je? (er naar toe gaan of verder lopen)')
                            except:
                                while True:
                                    try:
                                        print("Dat is niet een keuze!(kies er naar toe gaan of verder lopen!)")
                                        keuze_10 = input('je kunt kiezen om er naar toe te gaan of om verder te lopen wat doe je? (er naar toe gaan of verder lopen)')
                                        break
                                    except:
                                        print("Dat is niet een keuze!(kies er naar toe gaan of verder lopen!)")
                            if keuze_10 == 'er naar toe gaan':
                                print('je gaat er naar toe en loopt door een berenval')
                                print('je sterft aan je verwondingen')
                                print('game over')
                            elif keuze_10 == 'verder lopen':
                                print('je loopt verder en komt aan bij een huis')
                                try:
                                    keuze_11 = input('je kunt kiezen om aan te bellen of om weg te lopen wat doe je? (aanbellen of weglopen)')
                                except:
                                    while True:
                                        try:
                                            print("Dat is niet een keuze!(kies aanbellen of weglopen!)")
                                            keuze_11 = input('je kunt kiezen om aan te bellen of om weg te lopen wat doe je? (aanbellen of weglopen)')
                                            break
                                        except:
                                            print("Dat is niet een keuze!(kies aanbellen of weglopen!)")
                                if keuze_11 == 'aanbellen':
                                    print('je belt aan en er doet een oude vrouw open')
                                    try:
                                        keuze_12 = input('ze vraagt of je binnen wilt komen wat doe je? (binnenkomen of weglopen)')
                                    except:
                                        while True:
                                            try:
                                                print("Dat is niet een keuze!(kies binnenkomen of weglopen!)")
                                                keuze_12 = input('ze vraagt of je binnen wilt komen wat doe je? (binnenkomen of weglopen)')
                                                break
                                            except:
                                                print("Dat is niet een keuze!(kies binnenkomen of weglopen!)")
                                    if keuze_12 == 'binnenkomen':
                                        print('je komt binnen en de de vrouw sterft aan ouderdom. je krijgt haar huis.')
                                        print('je woont er en je sterft aan ouderdom. je ziet je familie en vrienden nooit meer en sterft alleen.')
                                    elif keuze_12 == 'weglopen':
                                        print('je loopt weg en verhongert')
                                        print('game over')
                                elif keuze_11 == 'weglopen':
                                    print('je loopt weg en verhongert')
                                    print('game over')
                        elif keuze_9 == 'rechts':    
                            print('je gaat rechts en vindt het einde van het bos')
                            print('je vindt je weg terug naar huis en leeft lang en gelukkig')
                            print('einde')
