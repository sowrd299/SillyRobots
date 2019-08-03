from gameManager import GameManager
from playerController import PlayerController

class OutOfTurnException(Exception):
    pass

class PlayerGameController(PlayerController):
    '''
    An ABSTRACT class that represents whatever controlls a card-game player
    Be that human, a networked client or an AI
    Manages the complete interface and UI with that entity
    '''
    
    def __init__(self, game : GameManager, player_ind : int):
        '''
        :param game: The game the player is playing in
        :param player_ind: the index of the player this control controls
        '''
        self.game = game
        self.player_ind = player_ind

    def _take_actions(self):
        raise NotImplementedError

    def take_actions(self) -> bool:
        '''
        Run this to allow the player to one or more actions on the game state
        May need to be called multiple times per turn
        Returns if the turn is over
        '''
        if not self.game.can_act(self.player_ind):
            return False
        return self._take_actions(self)

    def advance(self):
        '''
        To be called after take_actions returns true
        '''
        self.game.end_turn()
        self.game.start_turn()

    def may_play_card(self, card : "int or Card", pos : int):
        '''
        Returns if the controlled player may play the given card at the given location
        '''
        return self.game.may_play_card(self.player_ind, card, pos)

    def play_card(self, card : "int or Card", pos : int):
        '''
        Returns if the controlled player may play the given card at the given location
        '''
        self.game.play_card(self.player_ind, card, pos)

    def get_finished(self):
        return self.game.get_finished()