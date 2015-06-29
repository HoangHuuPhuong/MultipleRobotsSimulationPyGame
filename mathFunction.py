#/user/bin/env python
####Written by Phuong H. Hoang November, 2014
from math import sqrt, cos, sin, pi, tan

class cl_math_function(object):

    def __init__(self):
        test = 1
        
    def plan_circular_trajectory(self, p_start, p_center, angle_unit): # start and stop point
        traj = []
        number_inter = int(90/angle_unit)
        current_angle = 0
        for idx in range(0, number_inter):
            traj.append(self.find_point(p_start, p_center, current_angle))
            current_angle += angle_unit
        #print traj
        return traj

    def distance(self, p1, p2):
        return sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) + (p1[1] - p2[1])*(p1[1] - p2[1]))

    def find_center(self, p1, p2):
        dis_y = abs(p1[1] - p2[1])
        return [p1[0], p1[1] + 3*dis_y]

    def find_pstop(self, p_start, p_center):
        dis_y = abs(p_start[1] - p_center[1])
        return [p_center[0] + dis_y , p_center[1]]

    def find_point(self, p_start, p_center, angle):
        dis_y = abs(p_start[1] - p_center[1]) # radius
        x_delta = sin((angle*pi)/180.0)*dis_y
        x_p = p_start[0] + x_delta
        alpha = (180.0 - angle)/2
        petha = 90.0 - alpha
        y_delta = x_delta*tan((petha*pi)/180)
        y_p = p_start[1] + y_delta
        x_p = int(x_p)
        y_p = int(y_p)
        return [x_p, y_p]
