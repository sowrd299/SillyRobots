from playerController import PlayerController

from dialogueManager import DialogueManager
from dialogueSceneTextDisplay import DialogueSceneTextDisplay
from dialogueSpeachNode import DialogueSpeachNode

class LocalTextDialoguePlayerController(PlayerController):
    '''
    A class for an RPG player playing the game locally through text
    '''
    # TODO: connect this with the non-dialogue player controller?
    #       ... the problem there is that those are tied to individual (card) games
    # TODO: also create a dialogue player controller superclass...
    #       ... but that would be pretty useless in the current build

    def __init__(self, dialogue : DialogueManager):
        self.dialogue = dialogue
        self.disp = DialogueSceneTextDisplay()

    def show_current_node(self):
        text = self.disp.disp(self.dialogue.get_current_node())
        for line in text:
            print("\t"+line)
        return text

    def take_actions(self):
        text = self.show_current_node()
        if text: # don't wait up if nothing happened
            input_text = input()
        return True
        
    def advance(self):
        self.dialogue.update_node()

    def get_new_player_controllers(self):
        return self.dialogue.get_current_node().get_player_controllers()