autos = [
    {"merk": "Toyota", "model": "Camry", "maximale_snelheid": 180, "motorinhoud": 2.0},
    {"merk": "Honda", "model": "Accord", "maximale_snelheid": 200, "motorinhoud": 2.4},
    {"merk": "Ford", "model": "Focus", "maximale_snelheid": 190, "motorinhoud": 1.8},
    {"merk": "BMW", "model": "3 Serie", "maximale_snelheid": 250, "motorinhoud": 3.0},
    {"merk": "Mercedes", "model": "C-Klasse", "maximale_snelheid": 240, "motorinhoud": 2.5}
]

total_max_speed = 0
teller = 0

for auto in autos: 
    teller += 1
    total_max_speed += auto["maximale_snelheid"]   
    print(total_max_speed / teller)