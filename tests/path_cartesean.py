import time

#eDo serial number: 2404096

#joint limits
#j1	-178.90 to 178.90
#j2 -98.92 to 98.92
#j3 -98.92 to 98.92
#j4 -178.91 to 178.91
#j5 -103.41 to 103.41
#j6 -178.91 to 178.91
#j7 0 to 80.53mm

# from pyedo import edo
from edoSim import edosim as edo
#myedo = edo("10.42.0.49") # lan
myedo = edo("192.168.12.1") # lan

time.sleep(2)
myedo.init7Axes()
myedo.listen_JointState()
myedo.listen_CartesianPosition()

time.sleep(2)




input("Press ENTER to start PATH #1...")

x = -2.3703e-01
y = +5.1957e-01
z = +9.7262e-01
delta = 0.5
myedo.mov_to_default_pos()
time.sleep(2)
myedo.mov_cartesian(x, y, z)
time.sleep(2)
myedo.mov_cartesian(x + delta, +4.4457e-01, +9.7262e-01)
time.sleep(2)
myedo.mov_cartesian(x + delta, +4.4457e-01 - delta, +9.7262e-01)
time.sleep(2)
myedo.mov_cartesian(x, +4.4457e-01 - delta, +9.7262e-01)
time.sleep(2)

while True:

	state = myedo.get_JointState()

	print("v ", state['cartesianPosition'][0], state['cartesianPosition'][1], state['cartesianPosition'][2])

	time.sleep(0.5)	

time.sleep(120)

