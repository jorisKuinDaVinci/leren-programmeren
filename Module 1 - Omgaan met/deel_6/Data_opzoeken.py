def get_value(data: str, separator: str, position: int) -> str:
  splitted_strings = data.split(separator) # string splits itself into collection of strings
  if 0 <= position< len(splitted_strings):
    value = splitted_strings[position] # read value at position of split_values
  else:
    value = None
  return value