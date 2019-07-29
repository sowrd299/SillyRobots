from playerController import PlayerController

from boardTextDisplay import BoardTextDisplay

class LocalTextPlayerController(PlayerController):
    '''
    A player controller for local, human players
    playing with a text-based interface
    '''

    card_chars = "ABCDEFGHIJKLMNO" # characters to refer to cards

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
        # print a bunch of stuff
        print(("\n"*5) + ("V"*100) + ("\n"*3)) # spacer between turns
        self.disp_board()
        print("\n"*2)
        # TODO: input validating
        # get the player's action
        while True:
            input_text = input("~> [T] to end turn / Card [A...] and Position [1-4] to deploy: ").upper()
            # handle end of turn
            if input_text == "T":
                return True
            # play cards
            else:
                card = self.card_chars.index(input_text[0])
                pos = int(input_text[1])-1
                if self.may_play_card(card, pos):
                    self.play_card(card, pos)
                    print("~> Deploy sucessful")
                    return False
                else:
                    print("~> What nonsense is this? You can't put that there!")
        
        