from extratest0202 import *   

# aantal autos:
    
print(len(autos))

# hoe print ik alleen de auto met de kleinste moterinhoud! in 1 regel.

def get_motorinhoud(a):
    return a['motorinhoud']
auto_kleinste_motor = min(autos, key=get_motorinhoud)
print(auto_kleinste_motor)

auto_kleinste_motor2 = min(autos, key=lambda a: a['motorinhoud'])
print(auto_kleinste_motor2)