from juiste_antwoorden import *
naam = input('wat is je naam?')
if naam == naam_1:
    print('hallo ' + naam + 'dit zijn de juiste antwoorden: ' + juiste_antwoorden_1)
    print('hallo ' + naam + ' je loopt door een bos. je bent verdwaald')
else:
    print('hallo ' + naam + ' je loopt door een bos. je bent verdwaald')
keuze_1 = input('je staat voor een splitsing, welke kant kiest je? (links of rechts)')
while keuze_1 not in ['links', 'rechts']: 
            print("Dat is niet een keuze!(kies links of rechts!)")
            keuze_1 = input('je staat voor een splitsing, welke kant kiest je? (links of rechts)')
if keuze_1 == 'links':
    goed_antwoord_1 = 'nee'
    print('je loopt verder en komt een beer tegen, je rent weg maar de beer rent achter je aan en eet je op')
    print('game over')
    print('einde')
elif keuze_1 == 'rechts':
    print('je loopt verder en je komt aan bij een huis')
    goed_antwoord_1 = 'ja'
    keuze_2 = input('je kunt kiezen om aan te bellen of om weg te lopen, wat doe je? (aanbellen of weglopen)')
    while keuze_2 not in ['aanbellen', 'weglopen']:
                print("Dat is niet een keuze!(kies aanbellen of weglopen!)")
                keuze_2 = input('je kunt kiezen om aan te bellen of om weg te lopen, wat doe je? (aanbellen of weglopen)')
    if keuze_2 == 'aanbellen':
        goed_antwoord_2 = 'nee'
        keuze_2_5 = input('er doet niemand open je ziet een apparraat aan het huis hangen, je moet een code invoeren. a (code invoeren) of weglopen')
        while keuze_2_5 not in ['a', 'weglopen']: 
                    print("Dat is niet een keuze! kies a (code invoeren) of weglopen!")
                    keuze_2_5 = input('er doet niemand open je ziet een apparraat aan het huis hangen, je moet een code invoeren. a (code invoeren) of weglopen')
        if keuze_2_5 == 'a':
            print('je voert de code in')
            keuze_2_6 = input('voer de code in: ')
            if keuze_2_6 !='104':
                print('je hebt de code fout ingevoerd en het apparaat ontploft in je gezicht. je sterft.')
                print('game over')
                print('einde')
            elif keuze_2_6 == '104':
                print('je hebt de code goed ingevoerd en de deur gaat open.')
                keuze_3 = input('er staat een oude vrouw in het huis, ze vraagt of je binnen wilt komen, wat doe je? (b (naar binnen gaan) of weglopen)')
                while keuze_3 not in ['b', 'weglopen']:
                            print("Dat is niet een keuze! kies b (naar binnen gaan) of weglopen!")
                            keuze_3 = input('er staat een oude vrouw in het huis, ze vraagt of je binnen wilt komen, wat doe je? (b (naar binnen gaan) of weglopen)')
                if keuze_3 == 'b':
                    print('je komt binnen en de vrouw vraagt of je wat wilt drinken.')
                    keuze_4 = input('wil je drinken? (ja of nee)')
                    while keuze_4 not in ['ja', 'nee']:
                                print("Dat is niet een keuze!(kies ja of nee!)")
                                keuze_4 = input('wil je drinken? (ja of nee)')
                    if keuze_4 == 'ja':
                        print('je zegt ja en de vrouw geeft je een drankje, je drinkt het op en sterft')
                        print('game over')
                        print('einde')
                    elif keuze_4 == 'nee':
                        print('je zegt nee en de vrouw wordt boos, ze pakt een mes en steekt je neer')
                        print('game over')
                        print('einde')
                elif keuze_3 == 'weglopen':
                    print('je loopt weg en een beer valt je aan. je sterft aan je verwondingen.')
                    print('game over')
                    print('einde')
        if keuze_2_5 == 'weglopen':
            print('je loopt weg en een beer valt je aan. je sterft aan je verwondingen.')
            print('game over')
            print('einde')
    elif keuze_2 == 'weglopen':
        print('je loopt weg en komt aan bij een rivier')
        goed_antwoord_2 = 'ja'
        keuze_5 = input('er is een brug. je kunt kiezen om te zwemmen of om over de brug te lopen, wat doe je? zwemmen of brug (over de brug lopen)')
        while keuze_5 not in ['zwemmen', 'brug']:
                    print("Dat is niet een keuze! kies zwemmen of brug (over de brug lopen)!")
                    keuze_5 = input('er is een brug. je kunt kiezen om te zwemmen of om over de brug te lopen, wat doe je? zwemmen of brug (over de brug lopen)')
        if keuze_5 == 'brug':
            goed_antwoord_3 = 'nee'
            print('je loopt over de brug en de brug stort in, je valt in het water en verdrinkt')
            print('game over')
            print('einde')
        elif keuze_5 == 'zwemmen':
            print('je gaat zwemmen en komt veilig aan de overkant.')
            print('je loopt verder en komt aan bij een weg')
            goed_antwoord_3 = 'ja'
            keuze_6 = input('je kunt kiezen om te oversteken of verder door het bos te lopen wat doe je? oversteken of bos (door het bos lopen)')
            while keuze_6 not in ['oversteken', 'bos']:
                        print("Dat is niet een keuze! kies oversteken of bos (door het bos lopen)!")
                        keuze_6 = input('je kunt kiezen om te oversteken of verder door het bos te lopen wat doe je? oversteken of bos (door het bos lopen)')
            if keuze_6 == 'oversteken':
                goed_antwoord_4 = 'nee'
                print('je steekt over en wordt aangereden door een auto')
                print('game over')
                print('einde')
            elif keuze_6 == 'bos':
                print('je loopt door het bos en komt aan bij een zebrapad')
                goed_antwoord_4 = 'ja'
                keuze_7 = input('je kunt kiezen om over te steken of om te wachten wat doe je? (oversteken of wachten)')
                while keuze_7 not in ['oversteken', 'wachten']:
                            print("Dat is niet een keuze!(kies oversteken of wachten!)")
                            keuze_7 = input('je kunt kiezen om over te steken of om te wachten wat doe je? (oversteken of wachten)')
                if keuze_7 == 'wachten':
                    goed_antwoord_5 = 'nee'
                    print('je wacht en je wordt neergeschoten door een jager')
                    print('game over')
                    print('einde')
                elif keuze_7 == 'oversteken':
                    print('je steekt over en komt bij een ander bos.')
                    goed_antwoord_5 = 'ja'
                    print('je loopt verder en komt aan bij een huis met een bordje "te koop"')
                    keuze_8 = input('je kunt kiezen om het huis te kopen of om verder te lopen wat doe je? huis (huis kopen) of verder (verder lopen)')
                    while keuze_8 not in ['huis', 'verder']:
                                print("Dat is niet een keuze! kies huis (huis kopen) of verder (verder lopen!)")
                                keuze_8 = input('je kunt kiezen om het huis te kopen of om verder te lopen wat doe je? huis (huis kopen) of verder (verder lopen)')
                    if keuze_8 == 'huis':
                        goed_antwoord_6 = 'nee'
                        print('je koopt het huis en gaat er wonen')
                        print('je woont er 10 jaar en je sterft door een ziekte. je ziet je familie en vrienden nooit meer en sterft alleen.')
                        print('einde')
                    elif keuze_8 == 'verder':
                        goed_antwoord_6 = 'ja'
                        print('je loopt verder en komt bij een kruispunt')
                        keuze_9 = input('je kunt kiezen om links of rechts te gaan wat doe je? (links of rechts)')
                        while keuze_9 not in ['links', 'rechts']:
                                    print("Dat is niet een keuze! kies links of rechts!")
                                    keuze_9 = input('je kunt kiezen om links of rechts te gaan wat doe je? (links of rechts)')
                        if keuze_9 == 'links':
                            goed_antwoord_7 = 'nee'
                            print('je gaat links en ziet iets bekends')
                            keuze_10 = input('je kunt kiezen om er naar toe te gaan of om verder te lopen wat doe je? a (er naar toe gaan) of verder (verder lopen)')
                            while keuze_10 not in ['a', 'verder']:
                                        print("Dat is niet een keuze! kies a (er naar toe gaan) of verder (verder lopen)")
                                        keuze_10 = input('je kunt kiezen om er naar toe te gaan of om verder te lopen wat doe je? a (er naar toe gaan) of verder (verder lopen)')
                            if keuze_10 == 'a':
                                print('je gaat er naar toe en loopt door een berenval')
                                print('je sterft aan je verwondingen')
                                print('game over')
                                print('einde')
                            elif keuze_10 == 'verder':
                                print('je loopt verder en komt aan bij een huis')
                                keuze_11 = input('je kunt kiezen om aan te bellen of om weg te lopen wat doe je? (aanbellen of weglopen)')
                                while keuze_11 not in ['aanbellen', 'weglopen']:
                                            print("Dat is niet een keuze! kies aanbellen of weglopen!")
                                            keuze_11 = input('je kunt kiezen om aan te bellen of om weg te lopen wat doe je? (aanbellen of weglopen)')
                                if keuze_11 == 'aanbellen':
                                    print('je belt aan en er doet een oude vrouw open')
                                    keuze_12 = input('ze vraagt of je binnen wilt komen wat doe je? a (naar binnen gaan) of weglopen')
                                    while keuze_12 not in ['a', 'weglopen']:
                                                print("Dat is niet een keuze! kies a (naar binnen gaan) of weglopen!")
                                                keuze_12 = input('ze vraagt of je binnen wilt komen wat doe je? a (naar binnen gaan) of weglopen')
                                    if keuze_12 == 'a':
                                        print('je komt binnen en de de vrouw sterft later aan ouderdom. je krijgt haar huis.')
                                        print('je woont er en je sterft aan ouderdom. je ziet je familie en vrienden nooit meer en sterft alleen.')
                                        print('spel gewonnen!')
                                        print('einde')
                                    elif keuze_12 == 'weglopen':
                                        print('je loopt weg en verhongert')
                                        print('game over')
                                        print('einde')
                                elif keuze_11 == 'weglopen':
                                    print('je loopt weg en verhongert')
                                    print('game over')
                                    print('einde')
                        elif keuze_9 == 'rechts':    
                            print('je gaat rechts en vindt het einde van het bos')
                            goed_antwoord_7 = 'ja'
                            if goed_antwoord_1 == 'ja' and goed_antwoord_2 == 'ja' and goed_antwoord_3 == 'ja' and goed_antwoord_4 == 'ja' and goed_antwoord_5 == 'ja' and goed_antwoord_6 == 'ja' and goed_antwoord_7 == 'ja':
                                print('je vindt je weg terug naar huis en leeft lang en gelukkig')
                                print('je hebt alles goed gedaan!')
                                print('spel gewonnen!')
                                print('einde')
                            if not goed_antwoord_1 == 'ja' or not goed_antwoord_2 == 'ja' or not goed_antwoord_3 == 'ja' or not goed_antwoord_4 == 'ja' or not goed_antwoord_5 == 'ja' or not goed_antwoord_6 == 'ja' or not goed_antwoord_7 == 'ja':
                                print('je vindt je weg niet terug naar huis en verhongerd in het bos')
                                print('game over')
                                print('einde')
