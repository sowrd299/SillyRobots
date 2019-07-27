from card import Card
from subroutine import Subroutine

class RoboCard(Card):

    def __init__(self, name, factions, cost, bootup : Subroutine, program : [Subroutine]):
        '''
        :param bootup: a subroutine to run when spawned
        :param program: the robot's program
        '''
        super().__init__(name, factions, cost)
        self.bootup = bootup 
        self.program = program