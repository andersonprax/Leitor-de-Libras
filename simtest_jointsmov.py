from edoSim import edosim
import time


def simtest_jointsmov():
    edosim_test = edosim()
    edosim_test.init6Axes()
    edosim_test.mov_to_default_pos()

    edosim_test.setSpeed(1)
    edosim_test.mov_to_default_pos()
    edosim_test.mov_joints_pos(j1=90, j2=0, j3=0, j4=0, j5=0, j6=0)
    edosim_test.mov_joints_pos(j1=-90)
    time.sleep(5)
   #  #edosim_test.setSpeed(100)
   #  edosim_test.mov_joints_pos(0.5, 0.5, -0.5, -0.5, 0.5, 0.5)
   #  time.sleep(5)
   # # edosim_test.setSpeed(1)
   #  edosim_test.mov_joints_pos(-0.5, 0.5, 0.5, 0.5, 0.5, -0.5)
   #  time.sleep(5)
   #  edosim_test.mov_joints_pos(1, 0.5, 0.5, 0.5, 0.5, 1)
    #edosim_test.setSpeed(100)
    time.sleep(5)
    edosim_test.mov_to_default_pos()
    time.sleep(5)
    # edosim_test.finish()


if __name__ == '__main__':
    simtest_jointsmov()
