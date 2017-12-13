class Sizer(object):
	'''
	A class which represents the different sizing opportunities for
	various classes of things in other parts of the program

	:param tuple dimensions: The dimensions that the window is in - supports percentages
	'''

	def __init__(self, dimensions:tuple=(1280, 720), font_size=100, window=None):
		if window:
			self.dimensions = window.window.get_size()
		else:
			self.dimensions = dimensions
		self.font_size = 100
		self._original_width = self.dimensions[0]
		self.font_ratio = lambda: self.dimensions[0] / self._original_width
		self.window = window

	def __call__(self, *location):
		'''
		Gives you a set of x and y numbers for a given px/percentage

		:param str location: The location of your given item, with suffix px, em, or %
		:returns: A calculated tuple of where the item should be positioned
		:rtype: tuple
		'''

		if self.window:
			self.dimensions = self.window.window.get_size()

		location = list(location)
		for o, i in enumerate(location):
			if type(i) in [float, int]:
				continue
			elif 'px' in i:
				location[o] = float(i[:-2])
			elif '%' in i:
				location[o] = self.dimensions[o] * (float(i[:-1]) / 100)
			elif 'em' in i:
				location[o] = self.font_ratio() * self.font_size * float(i[:-2])
			else:
				location[o] = float(i)
		if len(location) == 1:
			return location[0]
		return tuple(location)
