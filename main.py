from gameManager import GameManager
from player import Player
from robotCard import RobotCard
from robot import Robot
from subroutine import Subroutine

from localTextPlayerController import LocalTextPlayerController

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
    players = [p1, p2]

    #setup the game management
    g = GameManager(players)
    player_controllers = [LocalTextPlayerController(g, i) for i,_ in enumerate(players)]

    return (g, player_controllers)

def run_test_game():
    g, player_controllers = start_test_game()
    g.start_game()
    # the main turn loop
    while not g.get_over():
        # run a turn
        g.turn_start()
        # let the player do stuff 
        while not player_controllers[g.get_current_player_ind()].take_actions():
            pass
        g.end_turn()
        print("\n~> NEXT TURN")
    print("~> Game Over)

if __name__ == "__main__":
    run_test_game()
