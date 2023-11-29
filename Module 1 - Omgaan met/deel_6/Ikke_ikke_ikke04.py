import re

def replace_separators(tekst: str) -> str:
  tekst = re.sub(r"\.|,|!|\?| en |omdat |zodat |want | wanneer |dat ", "|", tekst)
  return tekst

def split_sentences(tekst: str) -> list:
    sub_sentences = tekst.split("|") # split de text bij marker "|"
    return sub_sentences

def get_ego_score(tekst: str) -> int:
    sub_sentences = split_sentences(tekst)
    ego_score = 0
    for sentence in sub_sentences: # herhaal voor elke sentence in een list sentences
        sentence = sentence.strip() # verwijder leading en trailing spaces
        sentence = sentence.lower() # verander uppercase characters naar lowercase
        if len(sentence) > 0:
          words = sentence.split(' ') # split sentence in worden
          # eerste worden van sentence equal to ik?
          if len(words) >= 2 and (words[0] in ('ik','mijn') or words[1] in ('ik','mijn')):
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
tekst = replace_separators(tekst)
ego_score = get_ego_score(tekst)
print(ego_score)