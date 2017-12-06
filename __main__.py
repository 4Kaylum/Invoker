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
	cast = False
	first = False
	last_cast = None
	
	while not window.is_closed:

		# Add the frame ticker to the top left
		# window.draw_font('Tick {:X}'.format(counter), location=(0, 0), size=32)

		# Capture keydown and keyup events
		for i in window.events:
			if i.type == KEYDOWN:

				# Spell keys
				if i.key in [K_q, K_w, K_e]:
					text_colours[i.key] = Colour('red')
					pressed_keys.append(i.unicode.upper())
					cast = False

				# Cast key
				elif i.key == K_r:
					cast = True
					first = True

			elif i.type == KEYUP:
				if i.key in [K_q, K_w, K_e]:
					text_colours[i.key] = Colour('white')

		# Draw the QWE onto the screen
		window.draw_font('Q', location=(346, 540), size=300, colour=text_colours[K_q])
		window.draw_font('W', location=(542, 545), size=300, colour=text_colours[K_w])
		window.draw_font('E', location=(777, 545), size=300, colour=text_colours[K_e])

		# Output the goal spell you want to achieve
		window.draw_font('Goal: {.goal.name}'.format(invoker), location=(0, 100), size=150, colour=Colour('black'))

		# Output the socre
		window.draw_font('Score: {.score}'.format(invoker), location=(0, 0), size=150, colour=Colour('black'))

		# Temp output the last three characters
		window.draw_font(''.join(pressed_keys[-3:]), location=(0, 200), size=150, colour=Colour('blue'))

		# Get the working spell, if any
		x = invoker.cast(pressed_keys)

		# Determine whether a spell has been cast and no other buttons pressed
		if cast:

			# Run the first time that there has been no cast spell
			if first:
				last_cast = x
				first = False
				if last_cast == invoker.goal: invoker.score += 1
				invoker.make_goal()

			# The spell that's been cast
			pressed_keys = []
			l = (0, 300) if pressed_keys else (0, 200)
			window.draw_font('Cast: {0!s}'.format(last_cast), location=l, size=150, colour=Colour('blue'))

		# Run the program
		window.run()
		counter += 1


if __name__ == '__main__':
	main()

