import sim
from edorobot import EdoRobot

class edosim(EdoRobot):
    def __init__(self, host="192.168.12.1", host_sim='127.0.0.1', port=19999,
                 axes=7):  # default connection via wifi, connection via etehernet with '10.42.0.49'
        self.edo_ip = host
        self.client_id = sim.simxStart(host_sim, port, True, True, 5000, 5)
        super().__init__(self.client_id)
        self.axes = axes

    def init7Axes(self):
        self.init()

    def init6Axes(self):
        self.init()

    def calibAxes(self):
        pass

    def setSpeed(self, vel=1.0):
        pass

    def moveToHome(self):
        self.mov_to_default_pos()

    def moveJoints(self, j1=0.0, j2=0.0, j3=0.0, j4=0.0, j5=0.0, j6=0.0):
        self.mov_joints_pos(j1, j2, j3, j4, j5, j6)

    def moveCartesian(self, x=370, y=0, z=210, a=0, e=0, r=0):
        x, y, z = x/1000.0, y/1000.0, z/1000.0
        self.mov_cartesian(x, y, z)

    def moveCancel(self):
        pass

    def getJoints(self):
        j1_position = self.J1.pos
        j2_position = self.J2.pos
        j3_position = self.J3.pos
        j4_position = self.J4.pos
        j5_position = self.J5.pos
        j6_position = self.J6.pos

    def getCartesian(self):
        pass
    def get_JointState(self):
        self.update()
        joints_car_position = self.J6.pos
        joints_ang_position = [self.J1.rel_pos, self.J2.rel_pos, self.J3.rel_pos, self.J4.rel_pos, self.J5.rel_pos, self.J6.rel_pos]
        dict_ = {'cartesianPosition': joints_car_position, 'jointPosition': joints_ang_position}

        return dict_

    def getCartesian(self):
        pass

    def listen_JointState(self):
        pass

    def listen_CartesianPosition(self):
        pass

