# from player import Player # this might be slightly infite loopy

class Subroutine():
    '''
    A class for Subroutines robots carry out
    '''

    # common area of effect patterns
    single_target = [True]
    global_area = [True] * 7
    splash_area = [True] * 3 

    def __init__(self, accuracy : int = 0 , damage : int = 0 ,
            shield : int = 0 , glitch : int = 0,
            area : [bool] = [True], area_center_ind : int = -1):
        '''
        :param accuracy: How well the robot hits for damage
        :param damage: The amount of damagy
        :param shield: The amount of accuracy the robot shields against
        :param glitch: The amount the robot glitches the other
        :param area: A patern of where the effect hits
        :param area_center_index: Which index in the are pattern represents the robot's own collem. If -1, will center the list
        '''
        self.accuracy = accuracy
        self.damage = damage
        self.shield = shield
        self.glitch = glitch
        self.area = area
        self.area_center_ind = len(area) // 2 if area_center_ind == -1 else area_center_ind

    def __str__(self):
        r = ""
        if self.shield > 0:
            r += str(self.shield)+"S"
        if self.glitch > 0:
            r += str(self.glitch)+"G"
        if self.damage > 0:
            r += str(self.accuracy) + "A->" + str(self.damage)+"D"
        if not r:
            r += "n.op"
        return r

    def _resolve_shield(self, pos, controller):
        shl = self.shield
        if shl > 0 and 0 <= pos < len(controller.board):
            controller.add_shield(shl, pos)

    def _resolve_glitch(self, pos, target):
        glt = self.glitch
        if glt > 0 and 0 <= pos < len(target.board) and target.board[pos]:
            target.board[pos].take_glitch(glt)

    def _resolve_attack(self, pos, target):
        # deal with damage; by default, this ignores AoE
        acc = self.accuracy
        dmg = self.damage
        if acc > target.get_shield(pos) and dmg > 0:
            target.take_damage(dmg)

    def resolve(self, center_pos : int, controller, target):
        '''
        Applies the effects of the subroutine to the gamestate
        :param center_pos: where  the acting robot is assumed to be
        '''
        self._resolve_attack(center_pos, target)
        for i, in_area in enumerate(self.area):
            if in_area:
                pos = center_pos + i - self.area_center_ind
                self._resolve_shield(pos, controller)
                self._resolve_glitch(pos, target)