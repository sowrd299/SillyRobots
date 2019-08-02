from dialogueSpeachNode import DialogueSpeachNode
from character import Character

class DialogueSpeachTextDisplay():
    '''
    A class to render a speach node to next
    '''

    # display variables
    name_h_edge = "-"
    name_r_end = name_l_end = "+"
    bottom_r_end = "+ "
    bottom_l_end = " +"
    bottom_h_edge = "~"
    meta_text_edge = " / "

    def disp_name(self, character : Character):
        name = character.get_name()
        edge = self.name_l_end + self.name_h_edge * (len(name)-2) + self.name_r_end
        return [name, edge]

    def disp_meta_text(self, text : str):
        if text:
            return [self.meta_text_edge + text]
        else:
            return []

    def disp_text (self, text : str):
        l = self.bottom_l_end
        r = self.bottom_r_end
        edge = l + bottom_h_edge * (len(text)-len(l)-len(r)) + r
        return [text, edge]

    def disp(self, node : DialogueSpeachNode):
        # the name
        r = self.disp_name(node.get_character())
        # create the meta text, and afix it to the right of the name
        meta = self.disp_meta_text(node.get_meta_text())
        for i, _ in enumerate(r):
            if i >= len(meta):
                break
            r[i] += meta[i]
        # the main text
        r.extend(self.disp_text(node.get_text()))
        return r