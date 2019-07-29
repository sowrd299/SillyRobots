from subroutine import Subroutine
from player import Player
from robotCard import RobotCard

class GameManager():

    # game phases
    pre_phase = "PRE" # the game hasn't started
    main_phase = "MAIN" # the player is acting
    transition_phase = "TRANSITION" # turns are ending and starting

    def __init__(self, players : [Player]):
        self._players = players
        self._current_player_ind = 0
        self._phase = self.pre_phase 

    def resolve_subroutine(self, subroutine : Subroutine, pos : int, controller : Player, target : Player):
        '''
        Applies the affects of a subroutine
        '''
        # this is a bit hardcoded, but...
        acc = subroutine.accuracy
        dmg = subroutine.damage
        shl = subroutine.shield
        glt = subroutine.glitch
        if acc >= target.get_shield(pos) and dmg > 0:
            target.take_damage(dmg)
        if shl > 0:
            controller.set_shield(shl, pos)
        if glt > 0 and target.board[pos]:
            target.board[pos].take_glitch(glt)

    def _standardize_hand_card_input(self, player, card):
        # TODO: maybe this standardization should happen elsewhere...?
        '''
        Standarizes card input that may be in integer form
        '''
        if isinstance(card, int):
            return player.get_hand()[card]
        else:
            return card

    def may_play_card(self, player_ind : int, card : "int or RobotCard", pos : int):
        '''
        returns if the given player may play the given robot at the given spot
        '''
        # setup variables
        player = self._players[player_ind]
        card = self._standardize_hand_card_input(player, card)
        # do the test
        return player.may_play_robot(card, pos)

    def play_card(self, player_ind : int, card : "int or Card", pos : int):
        '''
        Plays a card from the given players hand at the given location
        '''
        # setup variables
        player = self._players[player_ind]
        card = self._standardize_hand_card_input(player, card)
        # play a robot
        if isinstance(card, RobotCard): 
            bootup = player.play_robot(card, pos)
            # manage bootup
            for sub in bootup:
                self.resolve_subroutine(sub)

    # game setup management

    def start_game(self):
        for player in self._players:
            # shuffle decks
            player.shuffle_deck()
            # draw starting hands
            player.draw(player.starting_hand_size)

    # turn management

    def _turn_start(self, player : Player, target : Player):
        # cleanup from last turn
        player.reset_shields()
        # run programs
        for i, robot in enumerate(player.board):
            if robot:
                s = robot.get_subroutine()
                self.resolve_subroutine(s, i, player, target)
                robot.next_subroutine()
        # cleanup
        self._phase = self.main_phase

    def turn_start(self):
        player = self._players[self._current_player_ind]
        target = self._players[(self._current_player_ind + 1) % len(self._players)]
        self._turn_start(player, target)

    def end_turn(self):
        # advance the turn counter
        self._current_player_ind += 1
        self._current_player_ind %= len(self._players)
        # cleanup
        for player in self._players:
            player.clear_robots()
        self._phase = self.transition_phase

    def get_current_player_ind(self):
        return self._current_player_ind

    def can_act(self, player_ind : int):
        '''
        Returns if the given player may act
        '''
        return self._current_player_ind == player_ind and self._phase == self.main_phase

    # getters

    def get_over(self):
        '''
        Returns if the game has ended
        '''
        return any(player.defeated() for player in self._players)
                
        