from robot import Robot 
from robotCardTextDisplay import RobotCardTextDisplay
from subroutine import Subroutine

class RobotTextDisplay(RobotCardTextDisplay):

    # override box style

    l_corner = "/"
    r_corner = "\\"

    # subroutine tracker decorum

    l_tracker = " {*"
    r_tracker = "*} "
    l_gltiched_tracker = " *%"
    r_gltiched_tracker = "%* "

    def __init__(self):
        self.robot = None

    # display functiions

    def disp_subroutine(self, i : int, sub : Subroutine):
        r = super().disp_subroutine(i, sub)
        if self.robot and self.robot._subroutine_track-1 == i:
            if self.robot.get_glitched():
                r = self.l_gltiched_tracker + r + self.r_gltiched_tracker
            else:
                r = self.l_tracker + r + self.r_tracker
        return r

    def _disp(self, *args, **kwargs) -> [str]:
        r = super()._disp(*args, **kwargs)
        if self.robot and self.robot.get_glitched():
            r.append(self.l_gltiched_tracker+"glitched"+self.r_gltiched_tracker)
        return r

    def disp(self, robot : Robot) -> [str]:
        '''
        Returns a text display for a given robot
        Each line is an entry in a list
        '''
        self.robot = robot # cache the robot for use elsewhere;
        # ...a bit hacky, but it works
        r = super().disp(robot._card)
        # apply glitched status
        # TODO: consolidate the "glitched" stuff?
        self.robot = None # uncash the robot, to prevent weird side effects
        return r