getal = 50 
som = getal
berekening = "50"
while som < 1000:
    getal = getal + 1
    som = som + getal   
    print(som)    
    berekening = berekening + " + " + str(getal)  
    print(f"{berekening} = {som}")     