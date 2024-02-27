from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
#color = robotArm.scan()
robotArm.speed = 2
robotArm.operate()

#for i in range(9):
    #robotArm.grab()
    #color = robotArm.scan()
    #if color == "red":
        #for i in range(9):
            #robotArm.moveRight()
        #robotArm.drop()
        #for i in range(9):
            #robotArm.moveLeft()
    #else:
        #robotArm.drop()
    #robotArm.moveRight()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

#Verplaats alle rode blokken naar het einde.

#Let op, de blokken zijn iedere keer anders als je het programma start!