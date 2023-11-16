from Data_opzoeken import get_value
toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
separator = ','
position= 8 # positie van Bram, eerste positie start met 0
value = get_value(toets_data, separator, position)
print(value) # prints: Bram:6