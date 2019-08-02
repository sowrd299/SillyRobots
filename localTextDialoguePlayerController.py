from dialogueManager import DialogueManager
from dialogueSceneTextDisplay import DialogueSceneTextDisplay

class LocalTextDialoguePlayerController():
    '''
    A class for an RPG player playing the game locally through text
    TODO: merge this with the non-dialogue player controller?
    '''

    def __init__(self, dialogue : DialogueManager):
        self.dialogue = dialogue
        self.disp = DialogueSceneTextDisplay()

    def show_current_node(self):
        text = self.disp.disp(self.dialogue.get_current_node())
        for line in text:
            print("\t"+line)

    def take_actions(self):
        self.show_current_node()
        input_text = input()
        self.dialogue.update_node()