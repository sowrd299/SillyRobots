from robotCardTextDisplay import RobotCardTextDisplay
from robotTextDisp import RobotTextDisplay

from card import Card
from gameManager import GameManager

class BoardTextDisplay():
    '''
    Displays the board state
    '''

    def __init__(self):
        self._card_disp = RobotCardTextDisplay()
        self._robot_disp = RobotTextDisplay()

    # display functions

    def disp_set(self, hand : [Card], disp):
        if hand:
            # handles each cards display and the default display for empty spaces
            disps = [disp.disp(card) if card else disp.disp_box([str(i+1)]) for i,card in enumerate(hand)]
            # assemle the displays together
            # r = [" ".join((card[i] if len(card) < i else " "*len(card[0])) for card in disps) for i in range(max(len(card) for card in disps))]
            r = []
            for i in range(max(len(card) for card in disps)):
                r.append("")
                for card in disps:
                    if i < len(card):
                        r[-1] += card[i]
                    else:
                        r[-1] += " " * len(card[0])
                    r[-1] += " "
            return r
        else: # handle empty hands
            return [""]

    def disp(self, game : GameManager):
        r = []
        for player in game._players:
            # name and health
            r.append("---{0}-{{{1} health}}---".format(player.name, len(player._deck)))
            r.append("")
            # robots
            r.append("s{0}/s{1}  robots:".format(player.get_total_size(), player.max_size))
            r.extend(self.disp_set(player.board, self._robot_disp))
            r.append("")
            # hand
            r.append("hand:")
            r.extend(self.disp_set(player._hand, self._card_disp))
        return r