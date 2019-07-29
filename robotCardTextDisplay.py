from cardTextDisplay import CardTextDispaly
from robotCard import RobotCard
from subroutine import Subroutine

class RobotCardTextDisplay(CardTextDispaly):

    # rendering variables

    type_name = "drofux"

    def __init__(self):
        pass

    # display functiions

    def disp_subroutine(self, i : int, sub : Subroutine):
        '''
        :param i: the index of the subroutine in the program
        '''
        return str(sub)

    def disp_bootup(self, sub : Subroutine):
        if sub: 
            return ["---bootup: {0}".format(self.disp_subroutine(-1, sub))]
        else:
            return []

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
        # the bootup
        r.extend(self.disp_bootup(card.bootup))
        # the program
        r.extend(self.disp_program(card.program))
        return r