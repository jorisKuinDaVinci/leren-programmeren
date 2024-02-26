from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
robotArm.grab()
for i in range(9):
    robotArm.moveRight()
robotArm.drop()
for i in range(8):
    robotArm.moveLeft()
robotArm.grab()
for i in range(7):
    robotArm.moveRight()
robotArm.drop()
for i in range(6):
    robotArm.moveLeft()
robotArm.grab()
for i in range(5):
    robotArm.moveRight()
robotArm.drop()
for i in range(4):
    robotArm.moveLeft()
robotArm.grab()
for i in range(3):
    robotArm.moveRight()
robotArm.drop()
for i in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
#Draai de volgorde van de blokken om.

#Je mag maximaal 15 regels code gebruiken inclusief de import, het laden van de robotarm en de wait