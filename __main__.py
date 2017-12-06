from pygame import Color as Colour
from pygame import KEYDOWN, KEYUP, K_q, K_w, K_e, K_r
from models.window import Window 
from models.invoker import Invoker
from models.block import Block


def main():
	'''
	The main function, provided *as* a function so as to deal with Sphinx's autodocs
	'''

	# Main globals
	window = Window()
	invoker = Invoker()

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

	# Pressed keys cache
	pressed_keys = []

	counter = 0
	draw = False
	
	while not window.is_closed:

		# Add the frame ticker to the top left
		window.draw_font('Tick {:X}'.format(counter), location=(0, 0), size=32)

		# Capture keydown and keyup events
		for i in window.events:
			if i.type == KEYDOWN:

				# Spell keys
				if i.key in [K_q, K_w, K_e]:
					text_colours[i.key] = Colour('red')
					pressed_keys.append(i.unicode.upper())
					draw = False

				# Cast key
				elif i.key == K_r:
					draw = True

			elif i.type == KEYUP:
				if i.key in [K_q, K_w, K_e]:
					text_colours[i.key] = Colour('white')

		# Draw the QWE onto the screen
		window.draw_font('Q', location=(346, 540), size=300, colour=text_colours[K_q])
		window.draw_font('W', location=(542, 545), size=300, colour=text_colours[K_w])
		window.draw_font('E', location=(777, 545), size=300, colour=text_colours[K_e])

		# Temp outputs - last three characters and cast spell
		window.draw_font(''.join(pressed_keys[-3:]), location=(700, 0), size=150, colour=Colour('blue'))
		x = invoker.cast(pressed_keys)
		if draw:
			window.draw_font('{0!s}'.format(x), location=(700, 100), size=150, colour=Colour('blue'))

		# Run the program
		window.run()
		counter += 1


if __name__ == '__main__':
	main()

