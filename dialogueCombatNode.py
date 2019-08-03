from dialogueNode import DialogueNode
from gameManager import GameManager
from playerController import PlayerController

class DialogueCombatNode(DialogueNode):
    '''
    A class for when a dialogue event procs combat
    Represents the start of combat, and does not deal with the end of it
    '''

    def __init__(self, game : GameManager, player_controllers : PlayerController, next_node):
        super().__init__(next_node)
        self.game = game
        self.player_controllers = player_controllers

    def start(self):
        self.game.start_game()
        self.game.turn_start()

    # GETTERS

    def get_game(self):
        return self.game

    def get_player_controllers(self):
        return self.player_controllers

    def make_finished_node(self, next_nodes : [DialogueNode]):
        '''
        Returns a new node that waits for the game started by this node to end
        :param next_nodes: the next nodes, indexed by which player wins to go to those nodes
        '''
        return DialogueCombatFinishedNode(self.game, next_nodes)

class DialogueCombatFinishedNode(DialogueNode):
    '''
    A node that waits for combat to be over before advancing the dialogue 
    '''

    def __init__(self, game : GameManager, next_nodes : [DialogueNode]):
        super().__init__(None)
        self.game = game
        self.next_nodes = next_nodes

    def get_finished(self):
        return self.game.get_finished()

    def get_next_node(self):
        return self.next_nodes[self.game.get_winner()]