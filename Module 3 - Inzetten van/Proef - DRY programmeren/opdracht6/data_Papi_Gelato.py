# Algemene teksten voor de Papi Gelato applicatie
TEKSTEN = {
    "welkom_tekst": "Welkom bij Papi Gelato.",
    "vraag_klant_type": "Bent u 1) een particuliere klant of 2) een zakelijke klant?",
    "ongeldige_invoer": "Sorry dat is geen optie die we aanbieden...",
    "teveel_bolletjes": "Sorry, zulke grote bakken hebben we niet.",
    "vraag_smaak": "Welke smaak wilt u voor bolletje nummer {bolletje_nummer}? A) Aardbei, C) Chocolade of V) Vanille?",
    "vraag_hoorntje_of_bakje": "Wilt u deze {aantal} bolletje(s) in een hoorntje of een bakje?",
    "bevestiging_bestelling": "Hier is uw {keuze} met {aantal} bolletje(s).",
    "vraag_topping": "Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?",
    "vraag_nog_meer": "Wilt u nog meer bestellen?",
    "afsluit_tekst": "Bedankt en tot ziens!",
    "vraag_liters": "Hoeveel liter wilt u?",
    "vraag_smaak_liter": "Welke smaak wilt u voor liter nummer {liter_nummer}? A) Aardbei, C) Chocolade of V) Vanille?",
    "ongeldig_aantal_liters": "Voer een geldig aantal liters in.",
}

# Prijsconfiguratie
PRIJZEN = {
    "bolletje": 0.95,  # Aangepaste prijs per bolletje
    "hoorntje": 1.25,
    "bakje": 0.75,
    "liter": 9.80,
    "toppings": {
        "Geen": 0.0,
        "Slagroom": 0.50,
        "Sprinkels": 0.30,  # Per bolletje
        "Caramel Saus Hoorntje": 0.60,
        "Caramel Saus Bakje": 0.90,
    },
}

# BTW-configuratie
BTW_TARIEF = {
    "standaard": 0.06,  # Aangepast naar 6%
}