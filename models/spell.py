class Spell(object):
    '''
    A spell that can be cast by the invoker

    :param str combo: The combo that defines this particular spell.
    :param str name: The name of this spell.
    '''


    def __init__(self, combo:str, name:str):
        self.combo = sorted(combo)
        self.name = name

    def __str__(self):
        return self.name
