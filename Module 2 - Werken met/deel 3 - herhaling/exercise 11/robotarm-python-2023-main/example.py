from RobotArm import RobotArm

robotArm = RobotArm('exercise 11')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
count_total = 10
count = 9
count_div = count - 1

for i in range(8):
    robotArm.moveRight()

for i in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        robotArm.moveRight()
        robotArm.drop()
        for i in range(count_total - count_div):
            robotArm.moveLeft()
        count -= 1
        count_div -= 1
    else:
        robotArm.drop()
        if i < 8:
            robotArm.moveLeft()
        count -= 1
        count_div -= 1

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
#Verplaats alle witte blokken één plek naar rechts. 
#Let op, de blokken zijn iedere keer anders als je het programma start!