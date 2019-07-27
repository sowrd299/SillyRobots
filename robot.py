from roboCard import RoboCard

class Robot():
    '''
    A class for robots actually in play
    '''

    def __init__(self, card : RoboCard):
        self._card = card
        self._subroutine_track = 0
        self.routine = None

    # BASIC OPPERATIONS

    def finished(self):
        '''
        Returns if the robot has finished it's program
        '''
        return self._subroutine_track >= len(self._card.program)

    def next_subroutine(self):
        '''
        Advances to the next subroutine; to be called once/turn
        '''
        if self.routine:
            pass
        else:
            self._subroutine_track += 1

    def get_subroutine(self):
        '''
        Return's the robot's current subroutine
        '''
        if self.finished():
            return None
        elif self.routine:
            # TODO: handle routine cards
            pass
        else:
            return self._card.program[self._subroutine_track]

    # COMBAT and GAME ACTIONS

    def take_glitch(self, i : int):
        '''
        Inflict i glitch onto the robot
        '''
        self._subroutine_track += i

    # STAT CHECKING

    def get_size(self):
        '''
        Returns the size taken up by this robot
        '''
        return self._card.cost + (self.routine._card.cost if self.routine else 0)

    def get_factions(self):
        '''
        Returns the factions the robot belongs to
        '''
        return self._card.factions