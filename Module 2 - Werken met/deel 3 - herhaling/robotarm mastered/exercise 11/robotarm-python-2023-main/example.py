from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 3

for c in range(8):
    robotArm.moveRight()
    
for a in range(9):
    robotArm.grab()
    color = robotArm.scan()
    if color == "white":
        print("wit")
        robotArm.moveRight()
        robotArm.drop()  
        robotArm.moveLeft() 
    else:
        robotArm.drop()
    if a != 8:
        robotArm.moveLeft()
            



robotArm.wait()
#Verplaats alle witte blokken één plek naar rechts. 
#Let op, de blokken zijn iedere keer anders als je het programma start!