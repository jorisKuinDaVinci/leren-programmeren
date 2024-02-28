from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
check_for_blocks = True
while check_for_blocks:
    robotArm.grab()
    if robotArm.scan() == "":
        check_for_blocks = False
    else:
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(9):
            robotArm.moveLeft()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
#Verdeel alle blokken over de lege plaatsen, zodra er geen blokken meer zijn moet de arm stoppen.