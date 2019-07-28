from cardTextDisplay import CardTextDispaly
from robotCard import RobotCard

class RobotCardTextDisplay(CardTextDispaly):

    def __init__(self):
        pass

    # display functiions
    

    def disp(self, card : Robot) -> [str]:
        '''
        Returns a text display for a given card
        Each line is an entry in a list
        '''