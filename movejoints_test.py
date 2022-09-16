import time

# from pyedo import eduedo as edo # Pyedo for real robot Control
from edoSim import edosim as eduedo # EdoSim for the Simulated Control

edo = eduedo('192.168.12.1')

# Init Axes
edo.init7Axes()

# Move to Default Position
edo.moveToHome()

input("Press ENTER to start Move Joints Test...")

# Start Movement
edo.moveJoints(0, 0, 90, 0, 0, 0)  # edge

time.sleep(4)

edo.moveJoints(90, 0, 90, 0, 0, 0)  # edge

time.sleep(4)

edo.moveJoints(178, 0, 90, 0, 0, 0)  # edge

time.sleep(4)

edo.moveJoints(90, 0, 90, 0, 0, 0)  # edge

time.sleep(4)

edo.moveJoints(0, 0, 90, 0, 0, 0)  # edge

time.sleep(4)

edo.moveJoints(-90, 0, 90, 0, 0, 0)  # edge

time.sleep(4)

edo.moveJoints(-178, 0, 90, 0, 0, 0)  # edge

time.sleep(4)

# Move to Default Position
edo.moveToHome()

