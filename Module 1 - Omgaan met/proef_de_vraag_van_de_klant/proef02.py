naam = input('wat is je naam?')
print('hallo ' + naam + ' je loopt in een bos. je bent verdwaald')
keuze_1 = input('je staat voor een splitsing, welke kant kiest je? (links of rechts)')
if keuze_1 == 'links':
    print('je loopt verder en komt een beer tegen, je rent weg maar de beer rent achter je aan en eet je op')
    print('game over')
elif keuze_1 == 'rechts':
    print('je loopt verder en je komt aan bij een huis')
    keuze_2 = input('je kunt kiezen om aan te bellen of om weg te lopen, wat doe je? (aanbellen of weglopen)')
    if keuze_2 == 'aanbellen':
        keuze_3 = input('er doet een oude vrouw open, ze vraagt of je binnen wilt komen, wat doe je? (binnenkomen of weglopen)')
        if keuze_3 == 'binnenkomen':
            print('je komt binnen en de vrouw vraagt of je wat wilt drinken.')
            keuze_4 = input('wil je drinken? (ja of nee)')
            if keuze_4 == 'ja':
                print('je zegt ja en de vrouw geeft je een drankje, je drinkt het op en sterft')
                print('game over')
            elif keuze_4 == 'nee':
                print('je zegt nee en de vrouw wordt boos, ze pakt een mes en steekt je neer')
                print('game over')
    elif keuze_2 == 'weglopen':
        print('je loopt weg en komt aan bij een rivier')
        keuze_5 = input('er is een brug. je kunt kiezen om te zwemmen of om over de brug te lopen, wat doe je? (zwemmen of over de brug lopen)')
        if keuze_5 == 'over de brug lopen':
            print('je loopt over de brug en de brug stort in, je valt in het water en verdrinkt')
            print('game over')
        elif keuze_5 == 'zwemmen':
            print('je gaat zwemmen en komt veilig aan de overkant.')
            print('je loopt verder en komt aan bij een weg')
            keuze_6 = input('je kunt kiezen om te oversteken of verder door het bos te lopen wat doe je? (oversteken of door het bos lopen)') 
            if keuze_6 == 'oversteken':
                print('je steekt over en wordt aangereden door een auto')
                print('game over')
            elif keuze_6 == 'door het bos lopen':
                print('je loopt door het bos en komt aan bij een zebrapad')
                keuze_7 = input('je kunt kiezen om over te steken of om te wachten wat doe je? (oversteken of wachten)')
                if keuze_7 == 'wachten':
                    print('je wacht en je wordt neergeschoten door een jager')
                    print('game over')
                elif keuze_7 == 'oversteken':
                    print('je steekt over en komt bij een ander bos.')
                    print('je loopt verder en komt aan bij een huis met een bordje "te koop"')
                    keuze_8 = input('je kunt kiezen om het huis te kopen of om verder te lopen wat doe je? (huis kopen of verder lopen)')
                    if keuze_8 == 'huis kopen':
                        print('je koopt het huis en gaat er wonen')
                        print('je woont er 10 jaar en je sterft door een ziekte. je ziet je familie en vrienden nooit meer en sterft alleen.')
                    elif keuze_8 == 'verder lopen':
                        print('je loopt verder en komt bij een kruispunt')
                        keuze_9 = input('je kunt kiezen om links of rechts te gaan wat doe je? (links of rechts)')
                        if keuze_9 == 'links':
                            print('je gaat links en ziet iets bekends')
                            keuze_10 = input('je kunt kiezen om er naar toe te gaan of om verder te lopen wat doe je? (er naar toe gaan of verder lopen)')
                            if keuze_10 == 'er naar toe gaan':
                                print('je gaat er naar toe en loopt door een berenval')
                                print('je sterft aan je verwondingen')
                                print('game over')
                            elif keuze_10 == 'verder lopen':
                                print('je loopt verder en komt aan bij een huis')
                                keuze_11 = input('je kunt kiezen om aan te bellen of om weg te lopen wat doe je? (aanbellen of weglopen)')
                                if keuze_11 == 'aanbellen':
                                    print('je belt aan en er doet een oude vrouw open')
                                    keuze_12 = input('ze vraagt of je binnen wilt komen wat doe je? (binnenkomen of weglopen)')
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
