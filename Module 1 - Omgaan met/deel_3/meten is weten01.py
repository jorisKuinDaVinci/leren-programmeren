getal_a = int(input("Geef een getal: "))
getal_b = int(input("Geef een getal: "))
#max = getal_a
#min = getal_b
if getal_a > getal_b:
    max = getal_a
    min = getal_b
    print("a is het grootste getal: " + str(max))
elif getal_a < getal_b:
    max = getal_b
    min = getal_a
    print("a is het kleinste getal: " + str(min))    
else:
    max = getal_a
    min = getal_a
    min == max
    print("a en b zijn even groot")

print("het minimum is: " + str(min))    
print("het maximum is: " + str(max))   