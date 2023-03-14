#!/usr/bin/env python
from robot_control_class import RobotControl

class ExamControl:

    def __init__(self):
        self.rc = RobotControl()

    def get_laser_readings(self):
        a = self.rc.get_laser(0)
        b = self.rc.get_laser(719)
        return b, a

    def main(self):
        self.rc.move_straight()
        while True:
            right = self.rc.get_laser(0)
            left = self.rc.get_laser(719)
            if (right == float("inf")) and (left == float("inf")):
                self.rc.stop_robot()
                break
