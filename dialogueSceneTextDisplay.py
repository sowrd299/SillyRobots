from dialogueSpeachTextDisplay import DialogueSpeachTextDisplay, DialogueSpeachNode
from dialogueManager import DialogueManager
from character import Character

class DialogueSceneTextDisplay():
    '''
    A class from managing the rendering of an entire scene of dialogue
    '''

    indent_step = 8

    def __init__(self, dm : Dialogue):
        self.clear_indents()
        self.speach_disp = DialogueSpeachTextDisplay()

    # MANAGING INDENDATIONS FOR DIFFERENT CHARACTS
    def clear_indents(self):
        self.character_indents = dict()

    def set_character_indents(self, indents : {Character : "int or str"}):
        for character, indent in indents:
            self.character_indents[character] = indent

    def get_indent(self, character : Character):
        r = self.character_indents[character]
        if isinstance(r, int):
            r = " " * r
        return r

    # 
    def disp(self)
        '''
        Displays the current node in the scene
        '''
        node = self.dialogue.get_node()
        if isinstance(node, DialogueSpeachNode):
            r = self.speach_disp.disp(node)
            # do the indentation
            indent = ""
            character = node.get_character() 
            if character not in self.character_indents:
                used_indent = set(self.character_indents.values())
                for i in range(8): # maximum default indent
                    # TODO: ignores text set indents
                    if i * self.indent_step not in used_indents:
                        self.character_indents[character] = i*self.indent_step
            indent = self.get_indent(character)
            r = [indent + line for line in r]
            # cleanup
            return r