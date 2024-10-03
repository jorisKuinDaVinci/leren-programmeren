#Wat voor type function(s) wordt/worden er in het volgende stukje code gebruikt:

def multiplier(n):
    return lambda a : a * n

def printAsText(anyType):
    print(str(anyType))

mytripler = multiplier(3)
printAsText(mytripler(2))

# A = build-in function. 
# B = User-defined function. 
# C = Anonymous function. 
# D = er wordt geen function gebruikt.

# Antwoord: A, B, C