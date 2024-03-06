from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
aantal = 10
for _ in range(5):
    robotArm.grab()
    aantal -= 1
    for i in range(aantal):
        robotArm.moveRight()
    robotArm.drop()
    aantal -= 1
    for i in range(aantal):
        robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
#Draai de volgorde van de blokken om.

#Je mag maximaal 15 regels code gebruiken inclusief de import, het laden van de robotarm en de wait