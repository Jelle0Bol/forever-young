from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for a in range(3):
    robotArm.moveRight()
robotArm.drop()
for b in range(3):
    robotArm.moveLeft()
robotArm.grab()
for c in range(2):
    robotArm.moveRight()
robotArm.drop()
for d in range(2):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveRight()
robotArm.grab()
robotArm.moveLeft()
robotArm.drop()
for e in range(2):
    robotArm.moveRight()
robotArm.grab()
for f in range(2):
    robotArm.moveLeft()
robotArm.drop()






# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()