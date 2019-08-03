class DialogueNode():
    '''
    An ABSTRACT class to represent events in a dialogue
    '''

    def __init__(self, next_node):
        '''
        :param next_node: the next node in the dialogue
        '''
        self._next_node = next_node

    def start(self):
        '''
        To be called when the node becomes the active node
        '''
        pass

    def set_next_node(self, next_node):
        self._next_node = next_node

    def get_next_node(self):
        return self._next_node

    def get_player_controllers(self):
        '''
        Returns any player controllers created by this event that now need to
        be managed
        '''
        return []

    def get_finished(self):
        '''
        Returns true if ready to move to the next node
        '''
        return True
