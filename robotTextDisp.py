from robot import Robot 
from robotCardTextDisplay import RobotCardTextDisplay
from subroutine import Subroutine

class RobotTextDisplay(RobotCardTextDisplay):

    # override box style

    l_corner = "/"
    r_corner = "\\"

    # subroutine tracker decorum

    l_tracker = "*"
    r_tracker = "*"

    def __init__(self):
        self.robot = None

    # display functiions

    def disp_subroutine(self, i : int, sub : Subroutine):
        r = super().disp_subroutine(i, sub)
        if self.robot and self.robot._subroutine_track == i:
            r = self.l_tracker + r + self.r_tracker
        return r

    def disp(self, robot : Robot) -> [str]:
        '''
        Returns a text display for a given robot
        Each line is an entry in a list
        '''
        self.robot = robot # cache the robot for use elsewhere;
        # ...a bit hacky, but it works
        return super().disp(robot._card)
        self.robot = None # uncash the robot, to prevent weird side effects