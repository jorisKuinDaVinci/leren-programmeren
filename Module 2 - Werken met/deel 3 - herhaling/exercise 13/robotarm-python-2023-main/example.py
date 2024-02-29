from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)

for block in range(7):
    
    robotArm.speed = 3
    # check_for_blocks = True
    robotArm.grab()
    if robotArm.scan() == "":
        break
    else:
        for _ in range(block+1):
            robotArm.moveRight();
        robotArm.drop()
        for _ in range(block+1):
            robotArm.moveLeft();




# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
#Verdeel alle blokken over de lege plaatsen, zodra er geen blokken meer zijn moet de arm stoppen.