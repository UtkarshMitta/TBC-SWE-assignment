# The class CarSimulator is a simple 2D vehicle simulator.
# The vehicle states are:
# - x: is the position on the x axis on a xy plane
# - y: is the position on the y axis on a xy plane
# - v is the vehicle speed in the direction of travel of the vehicle
# - theta: is the angle wrt the x axis (0 rad means the vehicle
#   is parallel to the x axis, in the positive direction;
#   pi/2 rad means the vehicle is parallel
#   to the y axis, in the positive direction)
# - NOTE: all units are SI: meters (m) for distances, seconds (s) for
#   time, radians (rad) for angles...
#
# (1)
# Write the method "simulatorStep", which should update
# the vehicle states, given 3 inputs:
#  - a: commanded vehicle acceleration
#  - wheel_angle: steering angle, measured at the wheels;
#    0 rad means that the wheels are "straight" wrt the vehicle.
#    A positive value means that the vehicle is turning counterclockwise
#  - dt: duration of time after which we want to provide
#    a state update (time step)
#
# (2)
# Complete the function "main". This function should run the following simulation:
# - The vehicle starts at 0 m/s
# - The vehicle drives on a straight line and accelerates from 0 m/s to 10 m/s
#   at a constant rate of 0.4 m/s^2, then it proceeds at constant speed.
# - Once reached the speed of 10 m/s, the vehicle drives in a clockwise circle of
#   roughly 100 m radius
# - the simulation ends at 100 s
#
# (3)
# - plot the vehicle's trajectory on the xy plane
# - plot the longitudinal and lateral accelerations over time

import math
import matplotlib.pyplot as plt

class CarSimulator():
    def __init__(self, wheelbase, v0, theta0):
        # INPUTS:
        # the wheel base is the distance between the front and the rear wheels
        self.wheelbase = wheelbase
        self.x = 0
        self.y = 0
        self.v = v0
        self.theta = theta0

    def simulatorStep(self, a, wheel_angle, dt):

        # Assuming wheel_angle is constant, i.e, the driver is holding the steering wheel at a constant angle
        # assuming dt is very small, hence only terms in final form linear in dt are considered
        if wheel_angle==0:
            self.x=self.x+self.v*math.cos(self.theta)*dt
            self.y=self.y+self.v*math.sin(self.theta)*dt
            self.v=self.v+a*dt
        else:
            v_t=self.v+a*dt
            omega=self.v/self.wheelbase*math.tan(wheel_angle)
            theta_t= self.theta+omega*dt
            R=self.wheelbase/math.tan(wheel_angle)
            x_t=self.x+R*math.sin(theta_t)-R*math.sin(self.theta)
            y_t=self.y+R*math.cos(self.theta)-R*math.cos(theta_t)
            self.x=x_t
            self.y=y_t
            self.v=v_t
            self.theta=theta_t


def main():
     wheelbase = 4  # arbitrary 4m wheelbase
     v0 = 0
     theta0 = 0
     simulator = CarSimulator(wheelbase, v0, theta0)
     dt = 0.1  # arbitrarily set the time step to 0.1 s
     t=0
     pos_x, pos_y=[simulator.x],[simulator.y]
     a_long, a_lat=[0],[0]
     times=[0]
     while simulator.v<10:
         simulator.simulatorStep(0.4,0,dt)
         t+=dt
         pos_x.append(simulator.x)
         pos_y.append(simulator.y)
         a_long.append(0.4)
         a_lat.append(0)
         times.append(t)
     wheel_angle_circle=-math.atan(wheelbase/100)
     while t<100:
         simulator.simulatorStep(0,wheel_angle_circle,dt)
         t+=dt
         pos_x.append(simulator.x)
         pos_y.append(simulator.y)
         a_long.append(0)
         a_lat.append(simulator.v**2/100) # centripetal acceleration
         times.append(t)

     plt.figure()
     plt.plot(pos_x,pos_y)
     plt.xlabel("x (m)")
     plt.ylabel("y (m)")
     plt.title("Vehicle Trajectory")
     plt.axis("equal")
     plt.grid(True)

     plt.figure()
     plt.plot(times,a_long,label="Longitudinal")
     plt.plot(times,a_lat,label="Lateral")
     plt.xlabel("Time (s)")
     plt.ylabel("Acceleration (m/s²)")
     plt.title("Accelerations over Time")
     plt.legend()
     plt.grid(True)

     plt.show()

main()
