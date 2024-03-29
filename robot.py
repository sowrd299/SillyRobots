from robotCard import RobotCard

class Robot():
    '''
    A class for robots actually in play
    '''

    def __init__(self, card : RobotCard):
        self._card = card # the card the robot was spawned from
        self._subroutine_track = 0 # tracks the next subroutine to run
        self._glitched = False # if the robot counts as "glitched"
        self.routine = None # the routine the robot is running

    # BASIC OPPERATIONS

    def finished(self):
        '''
        Returns if the robot has finished it's program
        '''
        return self._subroutine_track >= len(self._card.program)

    def next_subroutine(self):
        '''
        Advances to the next subroutine; to be called once/turn
        Clears "glitched" status
        '''
        if self.routine:
            pass
        else:
            self._subroutine_track += 1
        self._glitched = False

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
        Applies the glitched status
        '''
        self._subroutine_track += i
        self._glitched = True

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

    def get_card(self):
        return self._card

    def get_glitched(self):
        return self._glitched