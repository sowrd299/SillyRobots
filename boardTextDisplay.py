from robotCardTextDisplay import RobotCardTextDisplay
from robotTextDisp import RobotTextDisplay

from card import Card
from gameManager import GameManager
from player import Player

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

    def disp_player(self, player, invert = False, show_hidden = True):
        '''
        Renders the given player's section of the board
        :param invert: whether or not to turn the player's board upside down
        :param show_hidden: whether or not to show the player'd private information, like hand
        '''
        r = []
        # section functions
        def disp_spacer():
            r.append("")

        def disp_top(): # name and health
            r.append("---{0}-{{{1} health}}---".format(player.name, len(player._deck)))

        def disp_robots():
            # header
            r.append(" {{s{0}/s{1}}}\tdrofuxes:".format(player.get_total_size(), player.max_size))
            # create a function to disp positional shield values; move shields to bottom if inverting
            disp_shield = lambda i, robot : self.disp_shield(player.get_shield(i), robot, not invert)
            # make and indent the robot displays
            r.extend("\t"+line for line in self.disp_set(player.board, self._robot_disp, disp_shield))
        
        def disp_hand():
            # header
            size = len(player._hand)
            r.append(" hand:\t{{{0} card{1}}}".format(size, "" if size==1 else "s"))
            # make and indent the cards, if appropriate
            if show_hidden:
                r.extend("\t"+line for line in self.disp_set(player._hand, self._card_disp))
        
        # build and return
        disp_top()
        disp_spacer()
        if invert:
            disp_hand()
            disp_spacer()
            disp_robots()
        else:
            disp_robots()
            disp_spacer()
            disp_hand()
        
        return r

    def disp(self, game : GameManager, persp : int, omnisciant : bool = False):
        '''
        The main function to text-render the gamestate
        :param game: the gamestate to render
        :param persp: the index of the player from whose perspective to show the game
        :param omnisciant: if true, will show other player's hidden information
        '''
        r = []
        persp_player_disp = [] # a sepporate cach for the active player, to put them at the bottom
        for i, player in enumerate(game._players):
            player_disp = self.disp_player(player, i != persp, i == persp or omnisciant)
            if i == persp:
                persp_player_disp = player_disp
            else:
                r.extend(player_disp)
        r.extend(persp_player_disp)
        return r