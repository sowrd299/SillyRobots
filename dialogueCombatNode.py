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

    # GETTERS

    def get_game(self):
        return self.game

    def get_player_controllers(self):
        return self.player_controllers

    def make_finished_node(self, next_node):
        '''
        Returns a new node that waits for the game started by this node to end
        '''
        return DialogueCombatFinishedNode(self.game, next_node)

class DialogueCombatFinishedNode(DialogueNode):
    '''
    A node that waits for combat to be over before advancing the dialogue 
    '''

    def __init__(self, game : GameManager, next_node):
        super().__init__(next_node)
        self.game = game

    def get_finished(self):
        return self.game.get_finished()