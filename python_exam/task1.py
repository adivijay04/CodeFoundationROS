#!/usr/bin/env python
import math
from robot_control_class import RobotControl

def get_highest_lowest():
    rc = RobotControl()
    laser = rc.get_laser_full()
    laser_dict = {}
    op = []
    for i, ele in enumerate(laser):
        if not math.isinf(ele):
            laser_dict[i] = ele
    max_val = max(laser_dict.values())
    min_val = min(laser_dict.values())
    print(max_val, min_val)

    for k, v in laser_dict.items():
        if v == max_val:
            op.append(k)
            break

    for k, v in laser_dict.items():
        if v == min_val:
            op.append(k)
            break
    return op
