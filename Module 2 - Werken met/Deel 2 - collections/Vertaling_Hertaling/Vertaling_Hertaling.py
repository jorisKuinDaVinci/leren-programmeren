
tekst = input("Voer de tekst in die je wilt vertalen: ")
#tekst = "deur lopen buiten rennen snel raam binnen langzaam"
tekst.split()
dictionary = {
    "deur": 0,
    "lopen": 0,
    "buiten": 0,
    "rennen": 0,
    "snel": 0,
    "raam": 0,
    "binnen": 0,
    "langzaam": 0
}
print(tekst)
print(dictionary)
for i in tekst:
    if i in dictionary:
        dictionary[i] += 1   
if dictionary["deur"] > 0:
    tekst.replace("deur", "raam")
if dictionary["lopen"] > 0:
    tekst.replace("lopen", "rennen")
if dictionary["buiten"] > 0:
    tekst.replace("buiten", "binnen")
if dictionary["rennen"] > 0:
    tekst.replace("rennen", "lopen")
if dictionary["snel"] > 0:
    tekst.replace("snel", "langzaam")       
print(tekst)