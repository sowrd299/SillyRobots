from subroutine import Subroutine
from player import Player

class GameManager():

    def __init__(self, players : [Player]):
        self._players = players
        self._current_player_ind = 0

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

    def _turn_start(self, player : Player, target : Player):
        player.reset_shields()
        for i, robot in enumerate(player.board):
            if robot:
                s = robot.get_subroutine()
                self.resolve_subroutine(s, i, player, target)
                robot.next_subroutine()

    def turn_start(self):
        player = self._players[self._current_player_ind]
        target = self._players[self._current_player_ind + 1 % len(self._players)]
        self._turn_start(player, target)

    def end_turn(self):
        self._current_player_ind += 1

    def get_current_player_ind(self):
        return self._current_player_ind
                
        