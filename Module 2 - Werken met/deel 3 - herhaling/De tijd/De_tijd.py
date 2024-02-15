uur = 1
while uur < 25:
    if uur < 13:
        print(uur, "AM")
    else:
        print(uur - 12, "PM")
    uur += 1
