from playerGameController import PlayerGameController

class EncounterAiPlayerController(PlayerGameController):
    '''
    A player controller class for managing a simple "wilderness encounter" 
    -style enemy AI
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO: this feels like an invasion of privary, but I can't see a better way
        self.player = self.game.get_player(self.player_ind)

    def take_actions(self):
        '''
        A monoric algorithm that just wants to play all the cards it has
        '''
        for card in sorted(self.player.get_hand(), key = lambda x : x.cost, reverse = True):
            # TODO: this population algorithm is... bad...
            # ... especially sinse may play card is O(N) by itself
            for i, robot in enumerate(self.player.board):
                if self.may_play_card(card, i):
                    self.play_card(card, i)
                    break 
                if not robot: # if couldn't play card in an open space,
                    break     # ... give up trying to play it
        return True