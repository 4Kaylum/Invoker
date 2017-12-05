import pygame


class Window():
    '''
    Create the window object on which to draw and check events
    '''

    def __init__(self, *, dimensions:tuple=(1280, 720), caption:str="None", fps:int=30, colour:pygame.Color=pygame.Color('white')):
        '''
        Create the window object
        '''

        pygame.init()  
        pygame.font.init()  
        self.clock = pygame.time.Clock() 
        self.fps = fps
        self.events = []
        self.colour = colour

        # Create the window itself
        self.window = pygame.display.set_mode(dimensions)
        pygame.display.set_caption(caption)
        self.window.fill(colour)

        # Group of sprites
        self.sprites = pygame.sprite.Group()
        self.text_boxes = []

    def add_sprite(self, sprite:pygame.sprite.Sprite):
        '''
        Adds the given sprite to the window sprite group
        '''

        self.sprites.add(sprite)

    def add_sprites(self, *sprites):
        '''
        Adds all given sprites to the window sprite group
        '''

        for i in sprites:
            self.sprites.add(i)

    @property
    def is_closed(self):
        '''
        Returns false if the user pressed quit
        '''

        for e in self.events:
            if e.type == pygame.QUIT:
                return True
        return False

    def handle_event(self, event_type, function:callable):
        for i in self.events:
            if i.type == event_type:
                return function()
        return None

    def draw(self, reset:bool=True):
        if reset:
            self.window.fill(self.colour)
        self.sprites.draw(self.window)
        for i, o in self.text_boxes:
            self.window.blit(i, o)
        self.text_boxes = []

    def draw_font(self, text:str, location:tuple, *, size:int=16, colour:pygame.Color=pygame.Color('black')):
        '''
        Draw font onto the screen at a given coordinate
        '''

        font_obj = pygame.font.Font(None, size)
        font = font_obj.render(text, 1, colour)
        font.get_rect().center = location
        self.text_boxes.append((font, location))

    def run(self, draw:bool=True):
        '''
        Allows the actual window to tick and run and stuff
        '''

        if draw:
            self.draw()
            pygame.display.flip()
        self.clock.tick(self.fps)
        self.events = pygame.event.get()
