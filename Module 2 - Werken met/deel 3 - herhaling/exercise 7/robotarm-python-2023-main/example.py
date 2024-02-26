from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
robotArm.moveRight()
for i in range(6):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
for i in range(4):
    for i in range(2):
        robotArm.moveRight()
    for i in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()   

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

#Verplaats iedere stapel één plek naar links.

#Je mag maximaal 12 regels code gebruiken inclusief de import, het laden van de robotarm en de wait

#![Oefening 7](readme/exercise7.png)