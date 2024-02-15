
tekst = input("Geef een tekst: ")
tekst.split() 
dictionary = {
    "buiten": "binnen",
    "rennen": "lopen",
    "snel": "langzaam",
    "raam": "deur",
    "binnen": "buiten",
    "langzaam": "snel"
}
def hertaal(tekst, dictionary):
    hertaalde_tekst = ""
    for woord in tekst.split():
        if woord in dictionary:
            hertaalde_tekst += dictionary[woord] + " "
        if woord not in dictionary:
            hertaalde_tekst += woord + " "
    return hertaalde_tekst
print(hertaal(tekst, dictionary))