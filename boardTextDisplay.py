from robotCardTextDisplay import RobotCardTextDisplay
from robotTextDisp import RobotTextDisplay

from card import Card
from gameManager import GameManager

class BoardTextDisplay():
    '''
    Displays the board state
    This is the central display for the card game
    '''

    def __init__(self):
        self._card_disp = RobotCardTextDisplay()
        self._robot_disp = RobotTextDisplay()

    # display functions

    def disp_set(self, hand : [Card], disp, vernish : "(int, [str]) -> [str]" = None):
        '''
        Displays a collection of cards (or robots), such as a hand or a board
        Fills in blank spaces (None) with index numbers
        :param hand: the cards to display
        :param disp: the display to use to show the cards
        :param vernish: a function to alter the display of each card
        '''
        if hand:
            # handles each cards display and the default display for empty spaces
            disps = [disp.disp(card) if card else disp.disp_box([str(i+1)]) for i,card in enumerate(hand)]
            if vernish:
                disps = [vernish(i,card) for i,card in enumerate(disps)]
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

    def disp_shield(self, shield_value : int, robot_disp : [str], above = True):
        '''
        Adds on shield values to a disp of a robot as appropriate
        Adds empty space if shield is 0
        :param shield_value: the shield value to display
        :param robot_disp: the text rendering of the robot
        :param above: whether the shield should be above or bellow the robot
        '''
        # establish variables
        w = len(robot_disp[0])
        #   TODO: handle minimum width (5)
        shield_disp = []
        spacer = [ " " * w ]
        # construct the shield display
        if shield_value > 0:
            shield_disp = [
                " {0:<{1}}".format("/^^\\", w-1),
                " {0:<{1}}".format("\\{0:>2}/".format(shield_value), w-1),
                " {0:<{1}}".format(" \\/ ", w-1)
            ]
        else: # leave empty space if no shield
            shield_disp = spacer * 3
        # combine with a spacer and return
        if above:
            return shield_disp + spacer + robot_disp 
        else:
            return robot_disp + spacer + shield_disp


    def disp(self, game : GameManager):
        r = []
        for player in game._players:
            # name and health
            r.append("---{0}-{{{1} health}}---".format(player.name, len(player._deck)))
            r.append("")
            # robots
            r.append("s{0}/s{1}  robots:".format(player.get_total_size(), player.max_size))
            disp_shield = lambda i, robot : self.disp_shield(player.get_shield(i), robot)
            r.extend(self.disp_set(player.board, self._robot_disp, disp_shield))
            r.append("")
            # hand
            r.append("hand:")
            r.extend(self.disp_set(player._hand, self._card_disp))
        return r