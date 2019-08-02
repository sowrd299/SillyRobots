from dialogueManager import DialogueManager
from dialogueSpeachNode import DialogueSpeachNode
from dialogueCombatNode import DialogueCombatNode
from dialogueNode import DialogueNode
from character import Character

from gameManager import GameManager
from player import Player
from robotCard import RobotCard
from robot import Robot
from subroutine import Subroutine

from playerController import PlayerController
from localTextPlayerController import LocalTextPlayerController
from encounterAiPlayerController import EncounterAiPlayerController
from localTextDialoguePlayerController import LocalTextDialoguePlayerController


def build_dialogue(): 
    '''
    Creates dialogue
    '''

    char_buroad = Character("Buroad")
    char_kaoforp = Character("Kaoforp")

    # establish the dialogue in order as (character, text, metatext) tuples
    texts = [
        (char_kaoforp, "Welcome Arva! It is an honor you could join us!", "Arms held wide"),
        (char_buroad, "Sir, who is the new arival?", "A pleasant smile on his face"),
        (char_kaoforp, "She is our latest tranee. Arva of Unders. Millain says very good things about her.", None),
        (char_buroad, "Of Unders...", "Shoulders back, one eyebrow raised"),
        (char_kaoforp, "Yes, Squire, that is what I said", "Looking down, and begining to thumb a large book"),
        (char_buroad, "It is a pleaser to meet a lady from, so far a field", "Slowly"),
        (char_buroad, "...", "Eyes dart up"),
        (char_kaoforp, "Some days practices comes to you", "Looking off the same way"),
        (char_buroad, "Ranks! Ready! Hold ground!", "Raising drotome")
    ]

    # setup test combat
    players = build_players()
    combat_node = DialogueCombatNode(*setup_encounter_game(players), None)
    combat_node.set_next_node(combat_node.make_finished_node(None))

    # build the nodes backwords
    node = combat_node 
    while texts:
        character, text, meta_text = texts.pop(-1)
        node = DialogueSpeachNode(character, text, node, meta_text)

    return node

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
    robo_paladin = RobotCard("Paladin", ["Comlian"], 2, None, [sub_noop, sub_basic_shield, sub_basic_shield, Subroutine(accuracy=2, damage=2)])    
    robo_cavlier_orig = RobotCard("Cavalier", ["Comlian"], 2, None, [sub_basic_shoot, sub_basic_shield])
    robo_cavlier = RobotCard("Crested Cavalier", ["Comlian"], 2, None, [sub_basic_shield, sub_basic_shoot])
    robo_flash = RobotCard("Flash Interceptor", ["Comlian"], 3, Subroutine(shield=6), [Subroutine(shield=2), sub_noop])
    robo_interceptor = RobotCard("Lesser Interceptor", ["Comlian"], 1, Subroutine(shield=2), [Subroutine(shield=2)])
    robo_broad = RobotCard("Broadshield Pup", ["Comlian"], 2, None, [Subroutine(shield=2, area=Subroutine.splash_area), sub_basic_shoot])
    # UNDERS
    robo_stifler = RobotCard("Stifler", ["Unders"], 1, None, [sub_basic_shield, sub_basic_glitch])
    robo_snipe = RobotCard("Sneak-Snipe", ["Unders"], 2, None, [sub_basic_glitch, Subroutine(accuracy=3, damage=1)])
    robo_sassin = RobotCard("'Sassin", ["Unders"], 3, None, [Subroutine(glitch=3), sub_noop, sub_basic_shoot])
    robo_pure_sassin = RobotCard("Purist's 'Sassin", ["Unders"], 3, None, [Subroutine(glitch=3)])
    robo_cap = RobotCard("Capshot", ["Unders"], 1, Subroutine(accuracy=1, damage=1), [sub_noop] * 3)
    # WOLDEN
    robo_wolf = RobotCard("Lupoform", ["Wolden"], 2, None, [sub_noop, Subroutine(accuracy=1, damage=1), Subroutine(shield=2), Subroutine(accuracy=1, damage=1), sub_noop])
    robo_alfa = RobotCard("Lupoform First", ["Wolden"], 4, None, [sub_basic_shield, sub_noop, sub_basic_shield, Subroutine(accuracy=3, damage=4), sub_noop])
    robo_pup = RobotCard("Playful Pup", ["Wolden"], 1, None, [sub_noop, Subroutine(glitch=1, area=Subroutine.splash_area)])

    # make some players
    p1 = Player("Arva", [robo_chainer] * 3 + [robo_snipe] * 2 + [robo_machine] * 2 + [robo_stifler] * 2 + [robo_cap] * 3 + [robo_sunderer] * 2)
    #p1.board = [None, Robot(robo_chainer), Robot(robo_stifler), None]
    p2 = Player("Buroad", [robo_interceptor] * 2 + [robo_flash] * 1 + [robo_patience] * 3 + [robo_paladin] * 2 + [robo_cavlier] * 3 + [robo_broad] * 3)
    #p2.board = [Robot(robo_patience), None, Robot(robo_cavlier), None]
    p3 = Player("Pack of Lupoforms", [robo_alfa]*4 + [robo_wolf]*7 + [robo_pup]*3)

    # return the players
    ps = [p1, p2, p3]
    players = { p.name : p for p in ps }

    return players

# GAME SETUPS

def setup_dialogue(start_node : DialogueNode):
    d = DialogueManager()
    d.start_from(start_node)
    controller = LocalTextDialoguePlayerController(d)
    return (d, controller)

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
    name = player.get_name()
    prompt_str = "\n" * 100 + "{0}Here starts {1}'s next turn.\n{0}[ENTER]".format(prompt, name)
    input(prompt_str)

def no_transition(_, __):
    pass

# THE REAL "MAIN" STUFF

class ConflictingGameError(Exception):
    '''
    For when two games try to start at the same time
    '''
    pass

def run_game(d : DialogueManager, player_controller, transition):
    '''
    Runs the game, starting from a dialogue node
    '''
    # SETUP VARIABLES
    g = None
    player_controllers = []
    # THE MAIN LOOP
    while True:
        player_controller.take_actions()
        # see if we need to start a game
        game_data = d.get_game()
        if game_data:
            if not g:
                g, player_controllers = game_data
                g.start_game()
                g.turn_start()
            else:
                raise ConflictingGameError
        # if we are in a game, handle it
        # the main turn loop
        if g:            
            pc = player_controllers[g.get_current_player_ind()]
            transition(pc, g._players[g.get_current_player_ind()])
            # let the player do stuff 
            if pc.take_actions():
                # if the turn ended, advance the turn
                g.end_turn()
                g.turn_start()
            if g.get_finished():
                g = None
                player_controllers = []

if __name__ == "__main__":
    # run test dialogue and game
    dialogue = build_dialogue()
    run_game( *setup_dialogue(dialogue), no_transition)
