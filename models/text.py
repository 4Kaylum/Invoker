from pygame import Color as Colour
from pygame import font, Surface
from pygame.sprite import Sprite


class Block(Sprite):
    '''A plain coloured block that the window can draw'''

    def __init__(self, *, topleft:tuple=(0, 0), colour:Colour=Colour('black'), dimensions:tuple):
        super().__init__()
        self.image = Surface(dimensions)
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.topleft = topleft	
