class Character():
    '''
    A class for representing characters in the RPG world
    May or may not be player characters
    '''

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name()