from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.speed = 3
robotArm.moveRight()
for i in range(7):
    robotArm.grab()
    for i in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for i in range(8):
        robotArm.moveLeft()
robotArm.wait()

#Verplaats de stapel naar de rechterkant.

#Je mag maximaal 13 regels code gebruiken inclusief de import, het laden van de robotarm en de wait