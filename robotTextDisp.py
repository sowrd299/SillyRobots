from robot import Robot 
from robotCardTextDisplay import RobotCardTextDisplay

class RobotTextDisplay(RobotCardTextDisplay):

    # override box style

    l_corner = "/"
    r_corner = "\\"

    def __init__(self):
        pass

    # display functiions

    def disp(self, robot : Robot) -> [str]:
        '''
        Returns a text display for a given robot
        Each line is an entry in a list
        '''
        return super().disp(robot._card)