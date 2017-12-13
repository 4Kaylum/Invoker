from pygame import Color as Colour
from pygame import KEYDOWN, KEYUP, K_q, K_w, K_e, K_r
from pygame import mouse
from models.window import Window 
from models.invoker import Invoker
from models.block import Block
from models.sizer import Sizer


def main():
	'''
	The main function, provided *as* a function so as to deal with Sphinx's autodocs
	'''

	# Main globals
	DIMENSIONS = (1280, 720)
	FONT_SIZE = 100
	window = Window(dimensions=DIMENSIONS, resizable=True)
	invoker = Invoker()
	sizer = Sizer(window=window, font_size=FONT_SIZE)

	# Text colours
	text_colours = {
		K_q: Colour('white'),
		K_w: Colour('white'),
		K_e: Colour('white'),
		K_r: Colour('white'),
	}

	# Pressed keys cache
	pressed_keys = []

	counter = 0
	cast = False
	first = False
	last_cast = None
	
	while not window.is_closed:

		# Add the frame ticker to the top left
		# window.draw_font('Tick {:X}'.format(counter), location=(0, 250), size=32)

		# Create all the sprites needed
		window.sprites.empty()

		# Background block
		a = Block(dimensions=sizer('34%', '14%'))
		a.rect.midbottom = sizer('50%', '100%')

		# Left line
		b = Block(dimensions=sizer('5px', '14%'), colour=Colour('white'))
		b.rect.midbottom = sizer('41.5%', '100%')

		# Middle line
		c = Block(dimensions=sizer('5px', '14%'), colour=Colour('white'))
		c.rect.midbottom = sizer('50%', '100%')

		# Right line
		d = Block(dimensions=sizer('5px', '14%'), colour=Colour('white'))
		d.rect.midbottom = sizer('58.5%', '100%')

		# Add to window
		window.add_sprites(a, b, c, d)

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
					text_colours[i.key] = Colour('red')
					if len(pressed_keys) >= 3:
						cast = True
						first = True

			elif i.type == KEYUP:
				if i.key in [K_q, K_w, K_e, K_r]:
					text_colours[i.key] = Colour('white')

		# Get the font sizes
		full_size = int(sizer('1em'))
		half_size = int(sizer('.5em'))

		# Draw the QWE onto the screen
		window.draw_font('Q', location=sizer('35.0%', '88.9%'), size=full_size, colour=text_colours[K_q])
		window.draw_font('W', location=sizer('43.3%', '89.4%'), size=full_size, colour=text_colours[K_w])
		window.draw_font('E', location=sizer('52.5%', '89.2%'), size=full_size, colour=text_colours[K_e])
		window.draw_font('R', location=sizer('60.8%', '89.4%'), size=full_size, colour=text_colours[K_r])

		# Output the goal spell you want to achieve
		window.draw_font('Goal: {.goal.name}'.format(invoker), location=sizer(5, '.5em'), size=half_size, colour=Colour('black'))

		# Output the socre
		window.draw_font('Score: {.score}'.format(invoker), location=sizer(5, 5), size=half_size, colour=Colour('black'))

		# Temp output the last three characters
		window.draw_font(''.join(pressed_keys[-3:]), location=sizer(5, '1em'), size=half_size, colour=Colour('black'))

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

			# Draw spell onto screen
			pressed_keys = []
			l = sizer(5, '1.5em') if pressed_keys else sizer(5, '1em')
			window.draw_font('Cast: {0!s}'.format(last_cast), location=l, size=half_size, colour=Colour('black'))

		# Run the program
		window.run()
		counter += 1  # Frame tick


if __name__ == '__main__':
	main()

