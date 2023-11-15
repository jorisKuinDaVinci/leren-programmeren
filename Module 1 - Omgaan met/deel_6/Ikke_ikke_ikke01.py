import re
# replace alle separators "." , ",", " en ", "omdat ", "zodat ", "want ", " wanneer " en "dat ”by a marker "|"
def replace_separators(text: str) -> str:
  text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want | wanneer |dat ", "|", text)
  return text

def split_sentences(text: str) -> list:
    sub_sentences = text.split("|") # split de text on marker "|"
    return sub_sentences

def get_ego_score(text: str) -> int:
    ego_score = 0
    for sentence in sub_sentences: # repeat for every sentence in a list sentences
        sentence = sentence.strip() # remove leading and trailing spaces
        sentence = sentence.lower() # convert uppercase characters to lowercase
        if len(sentence) > 0:
          words = sentence.split(' ') # split sentence into words
          # first words of sentence equal to ik?
          if len(words) >= 2 and (words[0] in ('ik','mijn') or words[1] in ('ik','mijn')):
            ego_score += 1
    return ego_score

if __name__ == '__main__':
    text = """Geachte heer/mevrouw,
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
    text = replace_separators(text)
    sub_sentences = split_sentences(text)
    ego_score = get_ego_score(text)
    print(ego_score)