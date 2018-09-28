def drawClipped(self):
    screen.surface.blit(self._surf, (self.x-32, self.y -
                        self.height+30), (0, 0, 64, self.height))


def initBases():
    global bases
    bases = []
    bc = 0
    for b in range(3):
        for p in range(3):
            bases.append(Actor("base1"), midbottom=(150+(b*200)+(p*40), 520)
            bases[bc].drawClipped=drawClipped.__get__(bases[bc])
            bases[bc].height=60
            bc += 1

        def drawBases():
            for b in range(len(bases)):
                bases[b].drawClipped()
