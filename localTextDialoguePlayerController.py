from dialogueManager import DialogueManager
from dialogueSceneTextDisplay import DialogueSceneTextDisplay
from dialogueSpeachNode import DialogueSpeachNode

class LocalTextDialoguePlayerController():
    '''
    A class for an RPG player playing the game locally through text
    '''
    # TODO: merge this with the non-dialogue player controller?
    #       ... the problem there is that those are tied to individual (card) games

    def __init__(self, dialogue : DialogueManager):
        self.dialogue = dialogue
        self.disp = DialogueSceneTextDisplay()

    def show_current_node(self):
        text = self.disp.disp(self.dialogue.get_current_node())
        for line in text:
            print("\t"+line)

    def take_actions(self):
        if isinstance(self.dialogue.get_current_node(), DialogueSpeachNode):
            # TODO: not need to be so specific about this
            self.show_current_node()
            input_text = input()
        self.dialogue.update_node()
        # TODO: decide between controller and main who gets to call this