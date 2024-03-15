uur = 1
while uur < 24:
    if uur < 13:
        print(uur, "AM")
    else:
        print(uur - 12, "PM")
    uur += 1
print("12 AM")
