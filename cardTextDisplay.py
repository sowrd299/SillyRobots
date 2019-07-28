from card import Card

class CardTextDispaly():

    # box variables

    l_corner = "/"
    r_corner = "\\"
    h_edge = "-"
    v_edge = "|"

    # dispaly functions

    def disp_name(self, card : Card):
        return card.name

    def disp_cost_info(self, card : Card):
        t = "[s{0}\{1}]"
        factions = "/".join(card.factions)
        return t.format(card.cost, factions)

    def disp_title_line(self, card : Card):
        n = self.disp_name(card)
        c = self.disp_cost_info(card):
        return "{0} {1}".format(n, c)

    def disp_box(self, text : [str], width = 0, height = 0) -> [str]:
        '''
        Puts a box around the given text display
        '''
        w = width or max(len(s) for s in text)
        h = height or len(text)
        top = self.l_corner + self.h_edge*w + self.r_corner
        middle = [ "{0}{1:<{2}}{0}".format(self.v_edge, line, w) for line in text ]
        bottom = self.r_corner + self.h_edge*w + self.l_corner
        middle.insert(0, top)
        middle.append(bottom)
        return middle

    def _disp(self, card : Card):
        r = []
        r.append(self.disp_title_line(card))
        return r

    def disp(self, card : Card)
        r = self._disp(card)
        return self.disp_box(r)
        
