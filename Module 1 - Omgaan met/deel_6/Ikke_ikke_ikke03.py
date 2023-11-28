def string_to_lijst(zin_ik: str)-> [str]: 
    tekst_ik = zin_ik.lower() 
    print(tekst_ik)
    woorden_ik = tekst_ik.split(' ') 
    print(woorden_ik)
    return woorden_ik 
def bereken_hoeveel_keer_ik(tekst_ik: str): 
    aantal_ik = 0 
    
    ik_lijst = string_to_lijst(tekst_ik)
    for ik in ik_lijst: 
        if ik == 'ik': 
            aantal_ik += 1
    return aantal_ik 



tekst_ik = """Geachte heer/mevrouw,
    Ik wil graag solliciteren naar de functie van programmeur bij uw bedrijf.
    Ik ben de beste kandidaat voor deze functie omdat
    ik al jaren ervaring heb in deze branche en ik weet dat niemand anders mijn niveau van kennis en vaardigheden kan evenaren.
    Ik ben buitengewoon slim en
    in staat om snel nieuwe informatie te verwerken en te gebruiken om de beste beslissingen te nemen voor het bedrijf.
    Ik ben er zeker van dat ik binnen enkele weken op de hoogte zal zijn van alle zaken die spelen binnen uw bedrijf,
    en ik zal in staat zijn om snel resultaten te boeken en uw bedrijf naar de top te brengen.
    Mijn CV is overtuigend!
    Mijn referenties zijn heel positief over mij.
    Ik verdien daarom een plek in uw team.
    Ik kijk er naar uit om te horen wanneer ik op gesprek mag komen,
    zodat ik u persoonlijk kan overtuigen van mijn geschiktheid voor deze functie."""

print(bereken_hoeveel_keer_ik(tekst_ik)) 