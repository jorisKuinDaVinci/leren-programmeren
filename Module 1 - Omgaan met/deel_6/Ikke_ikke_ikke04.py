import re

def split_zinnen(tekst: str) -> list:
    print(tekst)
    tekst = re.sub(r"\.|,|!|\?| en |omdat |zodat |want | wanneer |dat ", "|", tekst)
    print(tekst)
    sub_zinnen = tekst.split("|") # split de tekst bij marker "|"
    return sub_zinnen

def pak_ego_score(tekst: str) -> int:
    sub_zinnen = split_zinnen(tekst)
    ego_score = 0
    for zin in sub_zinnen: # herhaal voor elke sentence in een list sentences
        zin = zin.strip() # verwijder leading en trailing spaces
        zin = zin.lower() # verander uppercase characters naar lowercase
        if len(zin) > 0:
          worden = zin.split(' ') # split sentence in worden
          # eerste worden van sentence equal to ik?
          if len(worden) >= 2 and (worden[0] in ('ik','mijn') or worden[1] in ('ik','mijn')):
            ego_score += 1
    return ego_score

tekst = """Geachte heer/mevrouw,
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
list_tekst = split_zinnen(tekst)#als je van een string een list maakt verander dan de naam van de string
ego_score = pak_ego_score(tekst)
print(ego_score)