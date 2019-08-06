from subroutine import Subroutine

class ReturnSubroutine(Subroutine):

    default_ally_area = [True, False, True]
    default_enemy_area = [True]

    def __init__(self, effect_enemy = False):
        super().__init__(area = self.default_enemy_area if effect_enemy else self.default_ally_area)
        self._effect_enemy = effect_enemy

    def __str__(self):
        return "Re"

    def _resolve_at(self, pos, controller, target):
        super()._resolve_at(pos, controller, target) # might as well get the extra millage
        player = target if self._effect_enemy else controller
        player.return_robot(pos)