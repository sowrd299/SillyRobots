class Subroutine():
    '''
    A class for Subroutines robots carry out
    '''

    def __init__(self, accuracy = 0 : int, damage = 0 : int, shield = 0 : int, glitch = 0 : int):
        '''
        :param accuracy: How well the robot hits for damage
        :param damage: The amount of damagy
        :param shield: The amount of accuracy the robot shields against
        :param glitch: The amount the robot glitches the other
        '''
        self.accuracy = accuracy
        self.damage = damage
        self.shield = shield
        self.glitch = glitch

    def __str__(self):
        r = ""
        if self.damage > 0:
            r += str(self.accuracy) + "A->" + str(self.damage)+"D"
        if self.shield > 0:
            r += str(self.shield)+"S"
        if self.glitch > 0:
            r += str(self.glitch)+"G"
        if not r:
            r += "n.op"