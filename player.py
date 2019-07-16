from card import Card
from subroutine import Subroutine
from roboCard import RoboCard
from robot import Robot

class Player():

    max_size = 9 # the maximum total size of robots the player may have in play

    def __init__(self, deck : [Card]):
        self._deck = deck
        self._hand = []
        self.board = [None] * 4 # BOARD SIZE IS IMPLEMENTED HERE

    # BASIC CARD/LIFE MANAGEMENT

    def draw(self, i : int):
        '''
        Adds i cards from top of deck to hand
        '''
        if i > len(self._deck):
            i = len(self.deck)
        self._hand.append(deck[:i])
        # TODO: sort the hand
        self._deck = deck[i:]

    def take_damage(self, i : int)
        '''
        Inflicts i damage on the player at the give point in space
        '''
        self.draw(i)

    def defeated(self)
        '''
        Returns whether or not this player has been defeated
        '''
        return len(self._deck) < 1

    # BOARD MANAGEMENT

    def spawn_robot(self, robot_card : RoboCard, pos : int) -> [Subroutine]:
        '''
        Spawns a robot at the given spot
        Returns any bootup subroutines caused by the spawn
        :param robot_card: the robot to spawn
        :param pos: the postion at which to spawn the robot
        '''
        assert 0 <= pos <= len(self.board), "Illegal board position "+str(pos)

        self.board[pos] = Robot(robot_card)
        return [robot_card.bootup] if robot_card.bootup else []

