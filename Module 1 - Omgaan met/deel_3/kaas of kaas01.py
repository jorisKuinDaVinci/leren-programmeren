input("is de kaas geel? ")
if input == "ja":
    input("zitten er gaten in? ")
    if input == "ja":
        input("is de kaas belachelijk duur? ")
        if input == "ja":
            print("Emmenthaler")
        else:
            print("Leerdammer")
    else:
        input("is de kaas hard als steen? ")
        if input == "ja":
            print("Pamigiano Reggiano")
        else:
            print("Goudse kaas")
if input == "nee":
    input("heeft de kaas blauwe schimmels? ")
    if input == "ja":
        input("heeft de kaas een korst? ")
        if input == "ja":
            print("Bleu de Rochbaron")
        else:
            print("Foume d'Ambert")
    else:
        input("heeft de kaas een korst? ")
        if input == "ja":
            print("Camembert")
        else:
            print("Mozzarella")            