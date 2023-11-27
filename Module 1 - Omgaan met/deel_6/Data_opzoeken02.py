def get_value(data: str, separator: str, position: int) -> str:
    splitted_strings = data.split(separator) 
  
    if 1 <= position <= len(splitted_strings):
      value_2 = position-1 
      value = splitted_strings[value_2]
    else:
      value = None
    return value

toets_data = 'muis,kat,hond'
separator = ','
position= 3 # positie van Bram, eerste positie start met 0
result = get_value(toets_data, separator, position)
print(result) # prints: Bram:6