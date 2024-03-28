import fruitmand
#Print de kleur, het gewicht en naam zoals onderstaand voorbeeld (dus volledig Nederlands) van het fruit met de langste naam, je mag alleen de code het juiste stuk fruit laten kiezen.
#voorbeeld van wat geprint moet worden: de "drakenfruit" (11 letters) heeft een rode kleur en weegt 600 gram
langste_naam_fruit = max(fruitmand.fruitmand, key=lambda x: len(x['name']))
print(f'de "{langste_naam_fruit["name"]}" ({len(langste_naam_fruit["name"])} letters) heeft een {langste_naam_fruit["color"]} kleur en weegt {langste_naam_fruit["weight"]} gram')