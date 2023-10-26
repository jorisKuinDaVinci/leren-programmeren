geel = input("is de kaas geel? ")
if geel == "ja":
    gaten = input("zitten er gaten in? ")
    if gaten == "ja":
        belachelijk_duur = input("is de kaas belachelijk duur? ")
        if belachelijk_duur == "ja":
            print("Emmenthaler")
        else:
            print("Leerdammer")
    else:
        hard_als_steen = input("is de kaas hard als steen? ")
        if hard_als_steen == "ja":
            print("Pamigiano Reggiano")
        else:
            print("Goudse kaas")
if geel == "nee":
    blauwe_schimmels = input("heeft de kaas blauwe schimmels? ")
    if blauwe_schimmels == "ja":
        korst = input("heeft de kaas een korst? ")
        if korst == "ja":
            print("Bleu de Rochbaron")
        else:
            print("Foume d'Ambert")
    else:
        korst_kaas = input("heeft de kaas een korst? ")
        if korst_kaas == "ja":
            print("Camembert")
        else:
            print("Mozzarella")            