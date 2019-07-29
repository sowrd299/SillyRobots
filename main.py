from gameManager import GameManager
from player import Player
from robotCard import RobotCard
from robot import Robot
from subroutine import Subroutine

from boardTextDisplay import BoardTextDisplay

def start_test_game() -> GameManager:

    # make some reuseable subs
    sub_basic_shoot = Subroutine(accuracy = 2, damage = 1)
    sub_basic_shield = Subroutine(shield = 3)
    sub_basic_glitch = Subroutine(glitch = 1)
    sub_noop = Subroutine()
    # make some robots
    robo_chainer = RobotCard("Chainer", [], 2, None, [sub_basic_shoot, sub_basic_glitch, sub_basic_glitch])
    robo_patience = RobotCard("Patient One", [], 3, None, [sub_noop, sub_noop, sub_noop, Subroutine(accuracy = 4, damage = 1, glitch = 1)])
    robo_paladin = RobotCard("Paladin", ["TABLE_COG"], 2, None, [sub_noop, sub_basic_shield, sub_basic_shield])    
    robo_cavlier = RobotCard("Cavalier", ["TABLE_COG"], 2, None, [sub_basic_shoot, sub_basic_shield])
    robo_stifler = RobotCard("Stifler", ["TRICKSTERS"], 1, None, [sub_basic_shield, sub_basic_glitch])
    # make some players
    p1 = Player("Arva", [robo_chainer] * 2)
    p1.board = [None, Robot(robo_chainer), Robot(robo_stifler), None]
    p2 = Player("Buroad", [robo_paladin] * 2)
    p2.board = [Robot(robo_patience), None, Robot(robo_cavlier), None]

    #setup the game management
    g = GameManager([p1, p2])

    return g

def disp_board(disp : BoardTextDisplay, game : GameManager):
    for line in disp.disp(game):
        print(line)

def run_test_game():
    disp = BoardTextDisplay()
    g = start_test_game()
    disp_board(disp, g)
    # the main turn loop
    while not g.get_over():
        g.turn_start()
        print("\n\n" + ("="*10) + "\n\n")
        disp_board(disp, g)
        input()
        g.end_turn()

if __name__ == "__main__":
    run_test_game()
