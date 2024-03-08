from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

robotArm.speed = 3

for stapel in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color != "":
        for i in range(9-stapel):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(9-stapel):
            robotArm.moveLeft()
    else:
        break

robotArm.wait()
#Verdeel alle blokken over de lege plaatsen, zodra er geen blokken meer zijn moet de arm stoppen.