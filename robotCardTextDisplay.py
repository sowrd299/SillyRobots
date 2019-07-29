from cardTextDisplay import CardTextDispaly
from robotCard import RobotCard
from subroutine import Subroutine

class RobotCardTextDisplay(CardTextDispaly):

    def __init__(self):
        pass

    # display functiions

    def disp_subroutine(self, i : int, sub : Subroutine):
        '''
        :param i: the index of the subroutine in the program
        '''
        return str(sub)

    def disp_program(self, program : [Subroutine]):
        subs = " / ".join(self.disp_subroutine(*sub) for sub in enumerate(program))
        return [subs]

    def _disp(self, card : RobotCard) -> [str]:
        '''
        Returns a text display for a given card
        Each line is an entry in a list
        '''
        # title bar
        r = super()._disp(card)
        r.append("--lorrow-")
        # the program
        r.extend(self.disp_program(card.program))
        return r