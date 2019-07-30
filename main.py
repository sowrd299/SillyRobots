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
    robo_chainer_orig = RobotCard("Chainer", [], 2, None, [sub_basic_shoot, sub_basic_glitch, sub_basic_glitch])
    robo_chainer = RobotCard("Chainer.II", [], 2, None, [Subroutine(glitch=2), sub_noop, sub_basic_shoot])
    robo_patience = RobotCard("Patient One", [], 3, None, [sub_noop, sub_noop, sub_noop, Subroutine(accuracy = 4, damage = 3), sub_noop])
    robo_sunderer = RobotCard("Lesser Sunderer", [], 3, None, [sub_noop, sub_basic_shoot] * 2)
    robo_machine = RobotCard("Nine-Wand", [], 2, None, [sub_noop] + [Subroutine(accuracy=1, damage=1)*3])
    robo_wrench = RobotCard("Bolt Wrench", ["Tinsly"], 2, Subroutine(glitch=1), [sub_noop])
    robo_fair = RobotCard("Fair Shot"), ["Tinsly"], 2, None, [sub_noop, Subroutine(accuracy=1, damage=3)]
    robo_paladin = RobotCard("Paladin", ["Comlian"], 2, None, [sub_noop, sub_basic_shield, sub_basic_shield, sub_basic_shoot])    
    robo_cavlier_orig = RobotCard("Cavalier", ["Comlian"], 2, None, [sub_basic_shoot, sub_basic_shield])
    robo_cavlier = RobotCard("Crested Cavalier", ["Comlian"], 2, None, [sub_basic_shield, sub_basic_shoot])
    robo_interceptor = RobotCard("Flash Interceptor", ["Comlian"], 3, Subroutine(shield=6), [Subroutine(shield=2), sub_noop])
    robo_interceptor = RobotCard("Lesser Interceptor"), ["Comlian"], 1, Subroutine(shield=2), [Subroutine(shield=2)]
    robo_stifler = RobotCard("Stifler", ["Unders"], 1, None, [sub_basic_shield, sub_basic_glitch])
    robo_snipe = RobotCard("Sneak-Snipe", ["Unders"], 2, None, [sub_basic_glitch, Subroutine(accuracy=3, damage=1)])
    robo_sassin = RobotCard("'Sassin", ["Unders"], 3, None, [Subroutine(glitch=3), sub_noop, sub_basic_shoot])
    robo_pure_sassin = RobotCard("Purist's 'Sassin", ["Unders"], 3, None, [Subroutine(glitch=3)])
    robo_cap = RobotCard("Capshot", ["Unders"], 1, Subroutine(accuracy=1, damage=1), [sub_noop] * 3)
    # make some players
    p1 = Player("Arva", [robo_chainer] * 2 + [robo_snipe] * 2 + [robo_sassin] * 2 + [robo_stifler] * 3 + [robo_cap] * 3 + [robo_sunderer] * 2)
    #p1.board = [None, Robot(robo_chainer), Robot(robo_stifler), None]
    p2 = Player("Buroad", [robo_interceptor] * 2 + [robo_patience] * 3 + [robo_paladin] * 2 + [robo_cavlier] * 2 + [robo_wrench] * 3 + [robo_sunderer] * 2)
    #p2.board = [Robot(robo_patience), None, Robot(robo_cavlier), None]
    players = [p1, p2]

    #setup the game management
    g = GameManager(players)
    player_controllers = [LocalTextPlayerController(g, i) for i,_ in enumerate(players)]

    return (g, player_controllers)

def hotseat_transition(prompt, name):
    prompt_str = "\n" * 100 + "{0}Here starts {1}'s next turn.\n{0}[ENTER]".format(prompt, name)
    input(prompt_str)

def run_test_game():
    g, player_controllers = start_test_game()
    g.start_game()
    # the main turn loop
    while not g.get_over():
        # run a turn
        g.turn_start()
        # let the player do stuff 
        pc = player_controllers[g.get_current_player_ind()]
        while not pc.take_actions():
            pass
        # cleanup
        g.end_turn()
        # todo: hotseat styles turn transition
        hotseat_transition(pc.prompt, g._players[g.get_current_player_ind()].name)
    print(player_controllers[0].prompt+"Game Over")

if __name__ == "__main__":
    run_test_game()
