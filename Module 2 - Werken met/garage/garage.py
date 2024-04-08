autos = [
    {"merk": "Toyota", "model": "Camry", "maximale_snelheid": 180, "motorinhoud": 2.0},
    {"merk": "Honda", "model": "Accord", "maximale_snelheid": 200, "motorinhoud": 2.4},
    {"merk": "Ford", "model": "Focus", "maximale_snelheid": 190, "motorinhoud": 1.8},
    {"merk": "BMW", "model": "3 Serie", "maximale_snelheid": 250, "motorinhoud": 3.0},
    {"merk": "Mercedes", "model": "C-Klasse", "maximale_snelheid": 240, "motorinhoud": 2.5}
]
def get_snelheid(auto):
    return auto["maximale_snelheid"]
gesorterde_autos = sorted(autos, key= get_snelheid)
gesorterde_autos = sorted(autos, key= lambda auto: auto["maximale_snelheid"])