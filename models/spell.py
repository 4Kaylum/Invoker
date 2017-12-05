class Spell(object):

    def __init__(self, combo, name):
        self.combo = sorted(combo)
        self.name = name

    def __str__(self):
        return self.name
