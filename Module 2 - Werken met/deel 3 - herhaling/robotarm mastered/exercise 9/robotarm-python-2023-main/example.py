from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for i in range(3):
    robotArm.moveRight()
for i in range(4):
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
robotArm.moveLeft()
for i in range(3):
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
robotArm.moveLeft()
for i in range(2):
    robotArm.grab()
    for i in range(5):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(5):
        robotArm.moveLeft()
robotArm.moveLeft()
robotArm.grab()
for i in range(5):
    robotArm.moveRight()
robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
#Verplaats alle stapels vijf stappen naar rechts.

#Je mag maximaal 13 regels code gebruiken inclusief de import, het laden van de robotarm en de wait