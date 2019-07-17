from subroutine import Subroutine
from player import Player

class GameManager():

    def resolve_subroutine(self, subroutine : Subroutine, pos : int, controller : Player, target : Player):
        '''
        Applies the affects of a subroutine
        '''
        # this is a bit hardcoded, but...
        acc = subroutine.accuracy
        dmg = subroutine.damage
        shl = subroutine.shield
        glt = subroutine.glitch
        if acc >= target.get_shield(pos) and dmg > 0:
            target.take_damage(dmg)
        if shl > 0:
            controller.set_shield(shl, pos)
        if glt > 0:
            target.board[pos].take_glitch(glt)

    def turn_start(self, player : Player, target : Player):
        player.reset_shields()
        for i, robot in enumerate(player.board):
            if robot:
                
        