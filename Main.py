from pygame import Color as Colour
from pygame import KEYDOWN, KEYUP, K_q, K_w, K_e
from models.window import Window 
from models.text import Block

# Window object
window = Window()

# Background block
x = Block(dimensions=(620, 175))
x.rect.midbottom = (640, 720)

# Left line
y = Block(dimensions=(5, 175), colour=Colour('white'))
y.rect.midbottom = (640 - 110, 720)

# Right line
z = Block(dimensions=(5, 175), colour=Colour('white'))
z.rect.midbottom = (640 + 110, 720)

# Add to window
window.add_sprites(x, y, z)

# Text colours
text_colours = {
	K_q: Colour('white'),
	K_w: Colour('white'),
	K_e: Colour('white'),
}

counter = 0
while not window.is_closed:

	# Add the frame ticker to the top left
	window.draw_font('Tick {:X}'.format(counter), (0, 0), size=32)

	# Capture keydown and keyup events
	for i in window.events:
		if i.type == KEYDOWN:
			if i.key in [K_q, K_w, K_e]:
				text_colours[i.key] = Colour('red')
		elif i.type == KEYUP:
			if i.key in [K_q, K_w, K_e]:
				text_colours[i.key] = Colour('white')

	# Draw the QWE onto the screen
	window.draw_font('Q', (346, 540), size=300, colour=text_colours[K_q])
	window.draw_font('W', (542, 545), size=300, colour=text_colours[K_w])
	window.draw_font('E', (777, 545), size=300, colour=text_colours[K_e])

	# Run the program
	window.run()
	counter += 1

