from playerController import PlayerController

from boardTextDisplay import BoardTextDisplay

class LocalTextPlayerController(PlayerController):
    '''
    A player controller for local, human players
    playing with a text-based interface
    '''

    card_chars_disp = "AbCdEFghIJklMNO" # characters to refer to cards
    card_chars = card_chars_disp.upper()
    end_turn_command = "T"
    prompt = "~> "

    def __init__(self, game, player_ind):
        super().__init__(game, player_ind)
        self.disp = BoardTextDisplay()

    # display functions

    def disp_board(self):
        hand_label = lambda i, _ : self.card_chars_disp[i]
        for line in self.disp.disp(self.game, self.player_ind, hand_label = hand_label):
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
            input_text = input(self.prompt+"[T] to end turn / Card [A...] and Position [1-4] to deploy: ").upper()
            # handle end of turn
            try:
                if input_text == self.end_turn_command:
                    return True
                # play cards
                else:
                        card = self.card_chars.index(input_text[0])
                        pos = int(input_text[1])-1
                        if self.may_play_card(card, pos):
                            self.play_card(card, pos)
                            print(self.prompt+"Deploy sucessful")
                            return False
                        else:
                            print(self.prompt+"What nonsense is this? You can't put that there!")
            except (ValueError, IndexError):
                print(self.prompt+"Huh? What did you say?") # basic error handling
        
        