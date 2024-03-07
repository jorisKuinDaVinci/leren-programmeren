from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 3
for stapel in range(1,5):
    for blokje in range(stapel):
        robotArm.grab()
        for i in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()

robotArm.wait()
#Verplaats alle stapels vijf stappen naar rechts.

#Je mag maximaal 13 regels code gebruiken inclusief de import, het laden van de robotarm en de wait