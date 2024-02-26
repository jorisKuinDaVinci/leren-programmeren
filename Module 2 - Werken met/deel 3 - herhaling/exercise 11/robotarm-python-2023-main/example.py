from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        for i in range(1):
            robotArm.moveRight()
            robotArm.drop()
            robotArm.moveLeft()
            robotArm.moveRight()      
    else:
        robotArm.drop()
    robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
#Verplaats alle witte blokken één plek naar rechts. 
#Let op, de blokken zijn iedere keer anders als je het programma start!