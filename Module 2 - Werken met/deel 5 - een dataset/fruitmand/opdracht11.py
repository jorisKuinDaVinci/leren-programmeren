from fruitmand import fruitmand
#Vraag aan de gebruiker om een kleur uit (alleen) de beschikbare kleuren van de fruitmand, als er toch een kleur gekozen wordt die niet in de fruitmand zit krijgt de gebruiker de melding: “De kleur {kleur} zit er niet in de fruitmand” en wordt de vraag opnieuw gesteld.
input_color = input('Kies een kleur uit de beschikbare kleuren van de fruitmand: ')
# let op de evisentie, beter in een variable!
if input_color not in set([fruit['color'] for fruit in fruitmand]):
    print(f'De kleur {input_color} zit er niet in de fruitmand')
    input_color = input('Kies een kleur uit de beschikbare kleuren van de fruitmand: ')
#Bepaal het verschil tussen het aantal ronde en niet ronde vruchten van de gekozen kleur.
round_count = len([fruit for fruit in fruitmand if fruit['color'] == input_color and fruit['round']])
#Print vervolgens het volgende als er van de gekozen kleur meer ronde dan niet ronde vruchten zijn:
#“Er zijn {X} meer ronde vruchten dan niet ronde vruchten in de kleur {kleur}”
if round_count > len([fruit for fruit in fruitmand if fruit['color'] == input_color and not fruit['round']]):
    print(f'Er zijn {round_count - len([fruit for fruit in fruitmand if fruit["color"] == input_color and not fruit["round"]])} meer ronde vruchten dan niet ronde vruchten in de kleur {input_color}')
#Print vervolgens het volgende als er van de gekozen kleur minder ronde dan niet ronde vruchten zijn:
#“Er zijn {X} minder ronde vruchten dan niet ronde vruchten in de kleur {kleur}”
if round_count < len([fruit for fruit in fruitmand.fruitmand if fruit['color'] == input_color and not fruit['round']]):
    print(f'Er zijn {len([fruit for fruit in fruitmand.fruitmand if fruit["color"] == input_color and not fruit["round"]]) - round_count} minder ronde vruchten dan niet ronde vruchten in de kleur {input_color}')
#Print vervolgens het volgende als er van de gekozen kleur evenveel ronde als niet ronde vruchten zijn:
#“Er zijn {X} ronde vruchten en {X} niet ronde vruchten in de kleur {kleur}”
if round_count == len([fruit for fruit in fruitmand.fruitmand if fruit['color'] == input_color and not fruit['round']]):
    print(f'Er zijn {round_count} ronde vruchten en {len([fruit for fruit in fruitmand.fruitmand if fruit["color"] == input_color and not fruit["round"]])} niet ronde vruchten in de kleur {input_color}')
