from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
for stapel_van_blokken in range (5):
    robotArm.moveRight()
    for i in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    if stapel_van_blokken < 4:
        robotArm.moveRight()  
robotArm.wait()

#Verplaats iedere stapel één plek naar links.

#Je mag maximaal 12 regels code gebruiken inclusief de import, het laden van de robotarm en de wait