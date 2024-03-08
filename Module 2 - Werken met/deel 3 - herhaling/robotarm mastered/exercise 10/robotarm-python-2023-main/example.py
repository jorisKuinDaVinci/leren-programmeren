from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
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

robotArm.wait()
#Draai de volgorde van de blokken om.

#Je mag maximaal 15 regels code gebruiken inclusief de import, het laden van de robotarm en de wait