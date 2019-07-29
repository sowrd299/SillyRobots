from cardTextDisplay import CardTextDispaly
from robotCard import RobotCard
from subroutine import Subroutine

class RobotCardTextDisplay(CardTextDispaly):

    def __init__(self):
        pass

    # display functiions

    def disp_program(self, program : [Subroutine]):
        return []

    def _disp(self, card : RobotCard) -> [str]:
        '''
        Returns a text display for a given card
        Each line is an entry in a list
        '''
        r = super()._disp(card)
        r.append("-lorrow-")
        r.extend(self.disp_program(card.program))
        return r