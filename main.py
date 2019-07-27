from gameManager import GameManager
from player import Player
from roboCard import RoboCard
from robot import Robot
from subroutine import Subroutine

def start_test_game() -> GameManager:

    # make some reuseable subs
    sub_basic_shoot = Subroutine(accuracy = 2, damage = 1)
    sub_basic_shield = Subroutine(shield = 3)
    sub_basic_glitch = Subroutine(glitch = 1)
    sub_noop = Subroutine()
    # make some robots
    robo_chainer = RoboCard("Chainer", [], 2, None, [sub_basic_shoot, sub_basic_glitch, sub_basic_glitch])
    robo_patience = RoboCard("Patience", [], 3, None, [sub_noop, sub_noop, sub_noop, Subroutine(accuracy = 4, damage = 1, glitch = 1)])
    robo_paladin = RoboCard("Pali", ["TABLE_COG"], 2, None, [sub_noop, sub_basic_shield, sub_basic_shield])    
    robo_cavlier = RoboCard("Cavalier", ["TABLE_COG"], 2, None, [sub_basic_shoot, sub_basic_shield])
    # make some players
    p1 = Player("Arva", [robo_chainer] * 2)
    p1.board = [Robot(robo_chainer), None, None, None]
    p2 = Player("Buroad", [robo_paladin] * 2)
    p2.board = [Robot(robo_patience), None, Robot(robo_cavlier), None]

    #setup the game management
    g = GameManager([p1, p2])

    return g

if __name__ == "__main__":
    g = start_test_game()
    g.turn_start()