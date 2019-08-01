from cardTextDisplay import CardTextDispaly
from robotCard import RobotCard
from subroutine import Subroutine

class RobotCardTextDisplay(CardTextDispaly):

    # rendering variables

    type_name = "drofux"

    # area stuff
    area_label = "area"
    area_symbol = "(@)"
    area_left = "[" # the left boarder of the area display
    area_right = "]" # ||, but right
    area_inter = "|" # between two area
    area_center_left = ">" # demark the "center space of the area"
    area_center_right = "<" 
    area_target = "@" # demark a space included in the area
    area_exclude = " " # demark a space excluded by the area

    # functions about the cards

    def is_area(self, sub : Subroutine):
        '''
        Returns weather or not to render the subroutine as AoE
        '''
        return sub.area != Subroutine.single_target 

    # display functiions

    def disp_subroutine(self, i : int, sub : Subroutine):
        '''
        :param i: the index of the subroutine in the program
        '''
        r = str(sub)
        if self.is_area(sub):
            r += self.area_symbol
        return r

    def disp_bootup(self, sub : Subroutine):
        if sub: 
            return ["---bootup: {0}".format(self.disp_subroutine(-1, sub))]
        else:
            return []

    def disp_program(self, program : [Subroutine]):
        subs = " / ".join(self.disp_subroutine(*sub) for sub in enumerate(program))
        return [subs]

    def _disp_area(self, area : [bool], center_ind : int):
        slots = []
        for i,slot in enumerate(area):
            t = self.area_target if slot else self.area_exclude 
            if i == center_ind:
                t = self.area_center_left + t + self.area_center_right
            slots.append(t)
        return [self.area_left + self.area_inter.join(slots) + self.area_right]

    def disp_area(self, program : [Subroutine]):
        r = []
        found_strings = set()
        for sub in program:
            if self.is_area(sub):
                text = self._disp_area(sub.area, sub.area_center_ind)
                if str(text) not in found_strings:
                    found_strings.add(str(text))
                    r.extend(text)
        return r

    def _disp(self, card : RobotCard) -> [str]:
        '''
        Returns a text display for a given card
        Each line is an entry in a list
        '''
        # title bar
        r = super()._disp(card)
        # the bootup
        r.extend(self.disp_bootup(card.bootup))
        # the program
        r.extend(self.disp_program(card.program))
        # the area of effect
        area = self.disp_area(card.program)
        if area:
            area_label = "-"+self.area_label
            area_label += "-"*(len(area[0])+1-len(area_label))
            r.append(area_label)
        r.extend(area)
        return r