from dialogueNode import DialogueNode

class UnexpectedEndOfDialogueError(Exception):
    pass

class DialogueManager():
    '''
    A class for managing dialogue in the RPG
    '''

    def __init__(self):
        self._node = None

    # NODE/FLOW MANAGAMENT

    def start_from(self, node : DialogueNode):
        '''
        Begins a dialogue with a given node
        '''
        self._node = node

    def get_current_node(self):
        '''
        Returns the current node in the dialogue
        '''
        return self._node

    def _next_node(self):
        '''
        Adavances dialogue to the next node
        '''
        self._node = self._node.get_next_node()
        # error handling
        if not isinstance(self._node, DialogueNode):
            raise UnexpectedEndOfDialogueError

    def update_node(self):
        '''
        Advances the state as necessary
        '''
        if self._node.get_finished():
            self._next_node()
