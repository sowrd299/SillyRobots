from gameManager import GameManager
from player import Player
from robotCard import RobotCard
from robot import Robot
from subroutine import Subroutine

from boardTextDisplay import BoardTextDisplay

def start_test_game() -> GameManager:
    '''
    Creates a test game state
    '''

    # make some reuseable subs
    sub_basic_shoot = Subroutine(accuracy = 2, damage = 1)
    sub_basic_shield = Subroutine(shield = 3)
    sub_basic_glitch = Subroutine(glitch = 1)
    sub_noop = Subroutine()
    # make some robots
    robo_chainer = RobotCard("Chainer", [], 2, None, [sub_basic_shoot, sub_basic_glitch, sub_basic_glitch])
    robo_patience = RobotCard("Patient One", [], 3, None, [sub_noop, sub_noop, sub_noop, Subroutine(accuracy = 4, damage = 1, glitch = 1)])
    robo_paladin = RobotCard("Paladin", ["Comlian"], 2, None, [sub_noop, sub_basic_shield, sub_basic_shield])    
    robo_cavlier = RobotCard("Cavalier", ["Comlian"], 2, None, [sub_basic_shoot, sub_basic_shield])
    robo_stifler = RobotCard("Stifler", ["Unders"], 1, None, [sub_basic_shield, sub_basic_glitch])
    robo_snipe = RobotCard("Sneak-Snipe", ["Unders"], 2, None, [sub_basic_glitch, Subroutine(accuracy=3, damage=1)])
    robo_sassin = RobotCard("'Sassin", ["Unders"], 3, None, [Subroutine(glitch=3)])
    # make some players
    p1 = Player("Arva", [robo_chainer] * 3 + [robo_snipe] * 2 + [robo_sassin])
    p1.board = [None, Robot(robo_chainer), Robot(robo_stifler), None]
    p2 = Player("Buroad", [robo_paladin] * 3 + [robo_cavlier] * 2 + [robo_stifler])
    p2.board = [Robot(robo_patience), None, Robot(robo_cavlier), None]

    #setup the game management
    g = GameManager([p1, p2])

    return g

def disp_board(disp : BoardTextDisplay, game : GameManager):
    for line in disp.disp(game, game.get_current_player_ind()):
        print("\t",line)

def run_test_game():
    disp = BoardTextDisplay()
    g = start_test_game()
    g.start_game()
    disp_board(disp, g)
    # the main turn loop
    while not g.get_over():
        print(("\n"*5) + ("V"*10) + ("\n"*5)) # spacer between turns
        g.turn_start()
        disp_board(disp, g)
        input()
        g.end_turn()

if __name__ == "__main__":
    run_test_game()
