import time

# from pyedo import eduedo as edo # Pyedo for real robot Control
from edoSim import edosim as eduedo  # EdoSim for the Simulated Control

edo = eduedo('192.168.12.1')

# Init Axes
edo.init7Axes()

input("Press ENTER to start Move Cartesian Test...")

# Move to Default Position
edo.moveToHome()

time.sleep(1)

edo.moveJoints(40.54, 12.22, -51.80, -36.92, -79.99, 23.25)

time.sleep(10)
edo.update()
print(f'base position = {edo.base.pos}')
edo.moveCartesian(-81.36, -87.20, 336.46, -178.96, 111.57, 178.95)

time.sleep(5)

edo.moveCartesian(-469.76, -87.20, 636.46, -178.96, 111.57, 178.95)

time.sleep(5)

edo.moveCartesian(-469.76, 0, 636.46, -178.96, 111.57, 178.95)

time.sleep(5)

edo.moveCartesian(-381.36, 0, 636.46, -178.96, 111.57, 178.95)

time.sleep(5)

edo.moveCartesian(-381.36, -87.20, 636.46, -178.96, 111.57, 178.95)

time.sleep(5)

edo.moveToHome()
