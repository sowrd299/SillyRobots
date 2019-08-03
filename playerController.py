class PlayerController():
    '''
    An ABSTRACT class for interfacing with a player
    or other intelegance that will advance the game state
    '''

    def take_actions(self) -> bool:
        '''
        Run this to allow the player to act
        Returns true when ready for "advance" to be called
        '''
        raise NotImplemented

    def advance(self):
        '''
        To be called after take_actions returns true
        '''
        raise NotImplemented

    def get_new_player_controllers(self) -> list:
        '''
        Returns additional player controllers that have joined the game
        ...as a resault of something this PC did
        '''
        return []

    def get_finished(self) -> bool:
        '''
        Returns True if this PC is no longer useful or needed
        '''
        return False