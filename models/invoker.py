from random import choice
from models.spell import Spell


class Invoker(object):
    '''
    The spell handler for the game at hand. This contains the score and goal of the player.
    '''

    spell_list = [
        Spell('QQQ', 'Cold Snap'),
        Spell('EEE', 'Sunstrike'),
        Spell('WWW', 'EMP'),
        Spell('QQW', 'Ghost Walk'),
        Spell('EEW', 'Meteor'),
        Spell('QQE', 'Ice Wall'),
        Spell('EEQ', 'Forge Spirit'),
        Spell('WWE', 'Alacrity'),
        Spell('QWE', 'Deafing Blast'),
        Spell('WWQ', 'Tornado'),
    ]

    def __init__(self):
        self.score = 0
        '''The score that the player has achieved.'''

        self.goal = choice(Invoker.spell_list)
        '''The spell that the player needs to cast.'''

    def make_goal(self):
        '''
        Creates a new goal for the player to achieve.
        '''

        self.goal = choice(Invoker.spell_list)

    def cast(self, spell_combo:list):
        '''
        Returns the spell of which the last three spell combinations create, or None of no
        spell could be cast.

        :param list spell_combo: The list of keys that have been pressed by the user. Only the last three will be used.
        :returns: The spell which the user has cast
        :rtype: :class:`Spell`
        '''

        # Filter out any but the last three characters
        spell_combo = [i.upper() for i in spell_combo[-3:]]
        if len(spell_combo) < 3:
            return None 

        # Invalid characters
        if not all([i in 'QWE' for i in spell_combo]):
            return None

        # Get the spell which was cast
        spell_combo.sort()
        casts = [i for i in Invoker.spell_list if i.combo == spell_combo]
        if casts:
            return casts[0]
        return None
