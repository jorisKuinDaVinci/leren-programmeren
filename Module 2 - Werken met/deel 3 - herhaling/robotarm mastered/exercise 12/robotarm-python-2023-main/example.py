from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
robotArm.speed = 3

for c in range(8):
    robotArm.moveRight()
    
for positie in range(8, -1, -1):
    robotArm.grab()
    color = robotArm.scan()
    if color == "red":
        print("rood")
        for move in range(9 - positie):
            robotArm.moveRight()
        robotArm.drop()  
        for move_2 in range(9 - positie):
            robotArm.moveLeft() 
    else:
        robotArm.drop()
    if positie != 0:
        robotArm.moveLeft()

robotArm.wait()

#Verplaats alle rode blokken naar het einde.

#Let op, de blokken zijn iedere keer anders als je het programma start!