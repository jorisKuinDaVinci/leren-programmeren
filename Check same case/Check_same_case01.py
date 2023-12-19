a = input("geef een letter: ")
b = input("geef een letter: ")
def same_case(a, b):
    if a.isletter() and b.isletter():
        if a.isupper() and b.isupper():
            return 1
        elif a.islower() and b.islower():
            return 1
        else:
            return 0
    else:
        return -1