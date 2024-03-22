import random
films = [
    {"title": "The Shawshank Redemption", "acteurs": ["Tim Robbins", "Morgan Freeman"], "jaar_verschijnen": 1994},
    {"title": "The Godfather", "acteurs": ["Marlon Brando", "Al Pacino"], "jaar_verschijnen": 1972},
    {"title": "The Dark Knight", "acteurs": ["Christian Bale", "Heath Ledger"], "jaar_verschijnen": 2008},
    {"title": "Pulp Fiction", "acteurs": ["John Travolta", "Uma Thurman"], "jaar_verschijnen": 1994},
    {"title": "Forrest Gump", "acteurs": ["Tom Hanks", "Robin Wright"], "jaar_verschijnen": 1994},
    {"title": "Inception", "acteurs": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"], "jaar_verschijnen": 2010},
    {"title": "The Matrix", "acteurs": ["Keanu Reeves", "Laurence Fishburne"], "jaar_verschijnen": 1999},
    {"title": "Schindler's List", "acteurs": ["Liam Neeson", "Ben Kingsley"], "jaar_verschijnen": 1993},
    {"title": "The Lord of the Rings: The Fellowship of the Ring", "acteurs": ["Elijah Wood", "Ian McKellen"], "jaar_verschijnen": 2001},
    {"title": "Goodfellas", "acteurs": ["Robert De Niro", "Joe Pesci"], "jaar_verschijnen": 1990}
]
# alle film titels onder elkaar
for film in films:
    print(film["title"])

#Netflix: ik weet niet wat ik wil kijken! Doe maar een random film
print(random.choice(films)["title"])

# titel en aantal acteurs van alle films!
for film in films:
    print(f"{film['title']} heeft {len(film['acteurs'])} acteurs")

# de titel en hoe oud de film is in jaren
for film in films:
    leeftijd = 2024 - film["jaar_verschijnen"]
    print(f"{film['title']} is {leeftijd} jaar oud")    

#  hoe oud/ welk jaartal is de ouste film
jaartallen = []
for film in films:
    jaartallen.append(film["jaar_verschijnen"])

oudste = min(jaartallen)
print(f"De oudste film is uit {oudste}")

# welke film is dat dan?
def getleeftijd(f):
    return(f["jaar_verschijnen"])
sorted_films = sorted(films, key=getleeftijd)
print(sorted_films[0]["title"])

# de nieuwste film maar dan met de lambda
sorted_reverse = sorted(films, key=lambda f: f["jaar_verschijnen"], reverse=True)
print(sorted_reverse[0]["title"])


#
jaar_gewenst = int(input("Welk jaar wil je een film?"))