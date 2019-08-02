from dialogueNode import DialogueNode
from character import Character

class DialogueSpeachNode(DialogueNode):
    '''
    A class for when someone says something durring a dialogue
    '''

    def __init__(self, character : Character, text : str, next_node, meta_text : str= ""):
        '''
        :param character: the character speaking
        :param text: what is said
        :param meta_text: context illustration
        '''
        super().__init__(next_node)
        self.character = character
        self.text = text
        self.meta_text = meta_text

    # GETTERS

    def get_character(self):
        return self.character

    def get_text(self):
        return self.text

    def get_meta_text(self):
        return self.meta_text

        