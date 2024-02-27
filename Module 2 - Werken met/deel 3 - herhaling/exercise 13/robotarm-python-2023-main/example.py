from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
#Verdeel alle blokken over de lege plaatsen, zodra er geen blokken meer zijn moet de arm stoppen.
for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(9):
            robotArm.moveLeft()
    else:
        robotArm.drop()
    robotArm.moveRight()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
#Verdeel alle blokken over de lege plaatsen, zodra er geen blokken meer zijn moet de arm stoppen.