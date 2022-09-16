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

#from pyedo import edo
from edoSim import edosim as edo
myedo = edo("10.42.0.49") # lan
#myedo = edo("192.168.12.1") # lan

time.sleep(2)
myedo.init7Axes()
myedo.listen_JointState()
myedo.listen_CartesianPosition()

time.sleep(2)

myedo.move_joint(ovr=100, j1=-178.9 + 0 * 17.89, j2=14.12, j3=97.55, j4=0, j5=-25.92, j6=45, j7=15)

input("Press ENTER to start PATH #2...")

for x in range(1, 21):
	if(x%2 == 0):
		myedo.move_joint(ovr=25, j1=-178.9 + x * 17.89, j2=14.12, j3=97.55, j4=0, j5=-25.92, j6=45, j7=15)
	else:
		myedo.move_joint(ovr=25, j1=-178.9 + x * 17.89, j2=14.12, j3=97.55, j4=0, j5=-4.62, j6=45, j7=15)

while True:

	state = myedo.get_JointState()

	print("v ", state['cartesianPosition'][0], state['cartesianPosition'][1], state['cartesianPosition'][2])

	time.sleep(0.5)	

time.sleep(120)

