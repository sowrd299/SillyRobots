from gameManager import GameManager
from player import Player
from robotCard import RobotCard
from robot import Robot
from subroutine import Subroutine

from playerController import PlayerController
from localTextPlayerController import LocalTextPlayerController
from encounterAiPlayerController import EncounterAiPlayerController

def build_players() -> GameManager:
    '''
    Creates all the cards and the decks with those cards
    '''

    # make some reuseable subs
    sub_basic_shoot = Subroutine(accuracy = 2, damage = 1)
    sub_basic_shield = Subroutine(shield = 3)
    sub_basic_glitch = Subroutine(glitch = 1)
    sub_noop = Subroutine()

    # make some robots
    # GENERIC
    robo_chainer_orig = RobotCard("Chainer", [], 2, None, [sub_basic_shoot, sub_basic_glitch, sub_basic_glitch])
    robo_chainer = RobotCard("Chainer.II", [], 2, None, [Subroutine(glitch=2), sub_noop, sub_basic_shoot])
    robo_sunderer = RobotCard("Lesser Sunderer", [], 3, None, [sub_noop, sub_basic_shoot] * 2)
    robo_machine = RobotCard("Nine-Wand", [], 2, None, [sub_noop] + [Subroutine(accuracy=1, damage=1)]*3)
    # TINZLY
    robo_wrench = RobotCard("Bolt Wrench", ["Tinzly"], 2, Subroutine(glitch=1), [sub_noop])
    robo_fair = RobotCard("Fair Shot", ["Tinzly"], 2, None, [sub_noop, Subroutine(accuracy=1, damage=3)])
    # COMLIAN
    robo_patience = RobotCard("Patient One", ["Comlian"], 3, None, [sub_noop]*3 + [Subroutine(accuracy = 4, damage = 3), sub_noop])
    robo_paladin = RobotCard("Paladin", ["Comlian"], 2, None, [sub_noop, sub_basic_shield, sub_basic_shield, sub_basic_shoot])    
    robo_cavlier_orig = RobotCard("Cavalier", ["Comlian"], 2, None, [sub_basic_shoot, sub_basic_shield])
    robo_cavlier = RobotCard("Crested Cavalier", ["Comlian"], 2, None, [sub_basic_shield, sub_basic_shoot])
    robo_flash = RobotCard("Flash Interceptor", ["Comlian"], 3, Subroutine(shield=6), [Subroutine(shield=2), sub_noop])
    robo_interceptor = RobotCard("Lesser Interceptor", ["Comlian"], 1, Subroutine(shield=2), [Subroutine(shield=2)])
    # UNDERS
    robo_stifler = RobotCard("Stifler", ["Unders"], 1, None, [sub_basic_shield, sub_basic_glitch])
    robo_snipe = RobotCard("Sneak-Snipe", ["Unders"], 2, None, [sub_basic_glitch, Subroutine(accuracy=3, damage=1)])
    robo_sassin = RobotCard("'Sassin", ["Unders"], 3, None, [Subroutine(glitch=3), sub_noop, sub_basic_shoot])
    robo_pure_sassin = RobotCard("Purist's 'Sassin", ["Unders"], 3, None, [Subroutine(glitch=3)])
    robo_cap = RobotCard("Capshot", ["Unders"], 1, Subroutine(accuracy=1, damage=1), [sub_noop] * 3)
    # WOLDEN
    robo_wolf = RobotCard("Lupoform", ["Wolden"], 2, None, [sub_noop, Subroutine(accuracy=1, damage=1), Subroutine(shield=2), Subroutine(accuracy=1, damage=1), sub_noop])
    robo_alfa = RobotCard("Lupoform First", ["Wolden"], 4, None, [sub_basic_shield, sub_noop, sub_basic_shield, Subroutine(accuracy=3, damage=4, sub_noop)])

    # make some players
    p1 = Player("Arva", [robo_chainer] * 3 + [robo_snipe] * 2 + [robo_machine] * 2 + [robo_stifler] * 2 + [robo_cap] * 3 + [robo_sunderer] * 2)
    #p1.board = [None, Robot(robo_chainer), Robot(robo_stifler), None]
    p2 = Player("Buroad", [robo_interceptor] * 2 + [robo_flash] * 1 + [robo_patience] * 3 + [robo_paladin] * 2 + [robo_cavlier] * 3 + [robo_wrench] * 3)
    #p2.board = [Robot(robo_patience), None, Robot(robo_cavlier), None]
    p3 = Player("Pack of Lupoforms", [robo_alfa]*4 + [robo_wolf]*10)

    # return the players
    ps = [p1, p2, p3]
    players = { p.name : p for p in ps }

    return players

# GAME SETUPS

def setup_encounter_game(players : {str : Player}):
    #setup the game management
    g = GameManager([players["Pack of Lupoforms"], players["Buroad"]])
    player_controllers = [EncounterAiPlayerController(g, 0), LocalTextPlayerController(g, 1)]
    return (g, player_controllers)

def setup_hotseat_game(players : {str : Player}):
    g = GameManager([players["Arva"], players["Buroad"]])
    player_controllers = [EncounterAiPlayerController(g, 0), LocalTextPlayerController(g, 1)]
    return (g, player_controllers)

# TRANSITIONS

def hotseat_transition(player_controller, player):
    prompt = player_controller.prompt
    name = player.name
    prompt_str = "\n" * 100 + "{0}Here starts {1}'s next turn.\n{0}[ENTER]".format(prompt, name)
    input(prompt_str)

def no_transition(_, __):
    pass

# THE REAL "MAIN" STUFF

def run_game(g : GameManager, player_controllers : [PlayerController], transition):
    g.start_game()
    # the main turn loop
    while not g.get_over():
        # run a turn
        g.turn_start()
        pc = player_controllers[g.get_current_player_ind()]
        transition(pc, g._players[g.get_current_player_ind()])
        # let the player do stuff 
        while not pc.take_actions():
            pass
        # cleanup
        g.end_turn()
    print(LocalTextPlayerController.prompt+"Game Over")

if __name__ == "__main__":
    players = build_players()
    run_game( *setup_encounter_game(players), no_transition )
