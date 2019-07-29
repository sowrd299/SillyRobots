from playerController import PlayerController

from boardTextDisplay import BoardTextDisplay

class LocalTextPlayerController(PlayerController):
    '''
    A player controller for local, human players
    playing with a text-based interface
    '''

    def __init__(self, game, player_ind):
        super().__init__(game, player_ind)
        self.disp = BoardTextDisplay()

    # display functions

    def disp_board(self):
        for line in self.disp.disp(self.game, self.player_ind):
            print("\t",line)
    
    # game control functions

    def take_actions(self):
        super().take_actions()
        print(("\n"*5) + ("V"*100) + ("\n"*5)) # spacer between turns
        self.disp_board()
        input()
        return True
        