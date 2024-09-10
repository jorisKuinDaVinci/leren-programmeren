#Breid nu het programma uit. 

#Je gaat een nieuwe functie maken die net zolang de functie van het vragen uitvoert totdat je het woord 'stop' invoert bij de vraag: “Toets enter om door te gaan of stop om te printen:” (let op: de eerste functie laat je met rust).

#De nieuwe functie is verrantwoordelijk voor het verzamelen en het stoppen vragen van de gegevens en heeft een output/return van een list

#Pas je output bestand aan zodat de verzamel functie word aangeroepen ipv de vragen functie en dan deze output geeft.

def vraag_naam_en_leeftijd():
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")
    return {"naam": naam, "leeftijd": leeftijd}

#functie = vraag_naam_en_leeftijd()
#print(f"{functie['naam']} is {functie['leeftijd']} jaar")

def verzamel_naam_en_leeftijd():
    