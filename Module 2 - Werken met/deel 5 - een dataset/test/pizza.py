pizza_menu = [
    {"naam": "Margherita", "diameter": 30, "ingrediënten": ["tomatensaus", "mozzarella", "basilicum"]},
    {"naam": "Pepperoni", "diameter": 35, "ingrediënten": ["tomatensaus", "mozzarella", "pepperoni"]},
    {"naam": "Hawaiian", "diameter": 40, "ingrediënten": ["tomatensaus", "mozzarella", "ham", "ananas"]},
    {"naam": "Quattro Stagioni", "diameter": 32, "ingrediënten": ["tomatensaus", "mozzarella", "ham", "champignons", "artisjokken", "olijven"]},
    {"naam": "Vegetarisch", "diameter": 38, "ingrediënten": ["tomatensaus", "mozzarella", "paprika", "ui", "champignons", "zwarte olijven"]},
    {"naam": "Quattro Formaggi", "diameter": 36, "ingrediënten": ["tomatensaus", "mozzarella", "gorgonzola", "fontina", "parmezaanse kaas"]},
    {"naam": "Tonno", "diameter": 33, "ingrediënten": ["tomatensaus", "mozzarella", "tonijn", "ui", "zwarte olijven"]},
    {"naam": "Prosciutto e Funghi", "diameter": 37, "ingrediënten": ["tomatensaus", "mozzarella", "ham", "champignons"]},
    {"naam": "Capricciosa", "diameter": 34, "ingrediënten": ["tomatensaus", "mozzarella", "ham", "champignons", "artisjokken", "zwarte olijven"]},
    {"naam": "Calzone", "diameter": 42, "ingrediënten": ["tomatensaus", "mozzarella", "ham", "champignons", "salami", "ricotta"]},
]


for pizza in pizza_menu:
    print(pizza["naam"])

aantal_pizza = len(pizza_menu)
print("Je hebt", aantal_pizza, "pizza's.")


   
aantal_met_ham = sum(1 for pizza in pizza_menu if "ham" in pizza["ingrediënten"])
print("Je hebt", aantal_met_ham, "pizza's met ham.")
