from card import Card
from subroutine import Subroutine
from robotCard import RobotCard
from robot import Robot

from random import shuffle

class Player():

    max_size = 9 # the maximum total size of robots the player may have in play
    board_size = 4 # how many slots for robots are on the board
    starting_hand_size = 4 # cards to draw at the start of the game

    def __init__(self, name, deck : [Card]):
        self._deck = deck
        self._hand = []
        self._discard = []
        self.name = name
        self.board = [None] * self.board_size 
        self.reset_shields()

    # SHIELD MANAGEMENT

    def get_shield(self, pos : int):
        '''
        Gets the shield value at the given position
        '''
        return self._shields[pos]

    def set_shield(self, val : int, pos : int):
        '''
        Sets the value of the shied in a given position
        '''
        self._shields[pos] = val
    
    def reset_shields(self):
        self._shields = [0] * self.board_size

    # BASIC CARD/LIFE MANAGEMENT

    def shuffle_deck(self):
        shuffle(self._deck)

    def draw(self, i : int):
        '''
        Adds i cards from top of deck to hand
        '''
        if i > len(self._deck):
            i = len(self.deck)
        self._hand.extend(self._deck[:i])
        # TODO: sort the hand
        self._deck = self._deck[i:]

    def take_damage(self, i : int):
        '''
        Inflicts i damage on the player at the give point in space
        '''
        self.draw(i)

    def defeated(self):
        '''
        Returns whether or not this player has been defeated
        '''
        return len(self._deck) < 1

    # BOARD MANAGEMENT

    def get_robots(self):
        '''
        Returns the robots the player has in play
        '''
        return filter(None, self.board)

    def _get_total_size(self, robots : [Robot]):
        '''
        Returns the total size of the given robots
        '''
        factions = set()
        size = 0
        for robot in robots:
            for faction in robot.get_factions():
                factions.add(faction)
            size += robot.get_size()
        return len(factions) + size

    def get_total_size(self):
        '''
        Returns the total size of the given robots
        '''
        return self._get_total_size(self.get_robots())

    def spawn_robot(self, robot_card : RobotCard, pos : int):
        '''
        Returns if the given robot may be legally played at the given position
        '''
        assert 0 <= pos <= len(self.board), "Illegal board position "+str(pos)
        return (not self.board[pos]) and self._get_total_size(self.get_robots() + [Robot(robot_card)]) <= self.max_size

    def spawn_robot(self, robot_card : RobotCard, pos : int) -> [Subroutine]:
        '''
        Spawns a robot at the given spot
        Returns any bootup subroutines caused by the spawn
        :param robot_card: the robot to spawn
        :param pos: the postion at which to spawn the robot
        '''
        assert 0 <= pos <= len(self.board), "Illegal board position "+str(pos)

        self.board[pos] = Robot(robot_card)
        return [robot_card.bootup] if robot_card.bootup else []

    def clear_robots(self):
        '''
        Removes finished robots from the board
        '''
        for i, robot in enumerate(self.board):
            if robot and robot.finished():
                self._discard.append(robot.get_card())
                self.board[i] = None