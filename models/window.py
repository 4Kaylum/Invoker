import pygame


class Window(object):
    '''
    Create the window object on which to draw and check events.
        
    :param tuple dimensions: (optional) The (x, y) dimensions of the window to be initialized.
    :param str caption: (optional) The caption that the window will be initialised with. Can be changed later with the :meth:`set_caption` method.
    :param int fps: (optional) The FPS that the screen will be run at. For this particular application, it doesn't really matter at all.
    :param pygame.Color colour: (optional) The background colour for the window.
    '''

    def __init__(self, *, dimensions:tuple=(1280, 720), caption:str="None", fps:int=30, colour:pygame.Color=pygame.Color('white')):
        # Init all the relevant Pygame stuff
        pygame.init()  
        pygame.font.init()  

        # Set the FPS
        self.clock = pygame.time.Clock() 
        self.fps = fps

        # Create the window itself
        self.window = pygame.display.set_mode(dimensions)
        pygame.display.set_caption(caption)
        self.colour = colour
        self.window.fill(colour)

        # All for internal usage
        self.sprites = pygame.sprite.Group()
        self.text_boxes = []
        self.events = []
        self.dimensions = dimensions  # Read only

    def set_caption(self, caption:str):
        '''
        Changes the caption for the window.

        :param str caption: The caption that the window will have its title set to.
        '''

        pygame.display.set_caption(caption)

    def add_sprite(self, sprite:pygame.sprite.Sprite):
        '''
        Adds the given sprite to the window sprite group.

        :param pygame.sprite.Sprite sprite: The sprite which will be added to the sprite group of the window.
        '''

        self.sprites.add(sprite)

    def add_sprites(self, *sprites):
        '''
        Adds all given sprites to the window sprite group.

        Used as a convenience to the user instead of calling :meth:`add_sprite` multiple times.

        Used as such:

        .. code-block:: python

            # Get your sprites
            x = Block()  # Assume block is a predefined sprite
            y = Block()

            # Instead of
            window.add_sprite(x)
            window.add_sprite(y)

            # Use
            window.add_sprites(x, y)

        :param pygame.sprite.Sprite: A list of sprites which will be added to the sprite group of the window.
        '''

        for i in sprites:
            self.sprites.add(i)

    @property
    def is_closed(self):
        '''
        Returns false if the user pressed quit.

        :returns: A boolean indicating whether or not the quit button has been pressed.
        :rtype: bool
        '''

        for e in self.events:
            if e.type == pygame.QUIT:
                return True
        return False

    def handle_event(self, event_type, function:callable):
        '''
        Calls a function should an event be present in the list of events for a given FPS tick.

        :param event_type: The event that is being compared.
        :param callable function: The function that will be called should the event be present. 
        '''

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

        :param str text: The text that should be written.
        :param tuple location: The (x, y) of where the text should be drawn.
        :param int size: (optional) The font size of the text.
        :param pygame.Color colour: (optional) The colour of the text.
        '''

        font_obj = pygame.font.Font(None, size)
        font = font_obj.render(text, 1, colour)
        font.get_rect().center = location
        self.text_boxes.append((font, location))

    def run(self, draw:bool=True):
        '''
        Allows the actual window to tick and run and stuff. Used to pump new events and optionally
        update the display.

        :param bool draw: (optional) Whether or not the display should be cleared/updated. 
        '''

        if draw:
            self.draw()
            pygame.display.flip()
        self.clock.tick(self.fps)
        self.events = pygame.event.get()
