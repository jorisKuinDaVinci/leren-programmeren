from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
for x in range(4):
    robotArm.grab()
    for x in range(2):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(2):
        robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for x in range(4):
    robotArm.moveRight()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()

#Verplaats de hele stapel blokken één plek naar rechts. Zorg ervoor dat de volgorde van de blokken gelijk blijft.