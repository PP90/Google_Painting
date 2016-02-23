DEFAULT=-1

class Point:
	x=DEFAULT
	y=DEFAULT
	value=DEFAULT

	def __init__(self, x=DEFAULT, y=DEFAULT, value=DEFAULT):
		self.x=x		
		self.y=y
		self.value=value

	def get_y(self):
		return self.y

	def get_x(self):
		return self.x

	def print_info(self):
		print "(x,y) value", self.x, self.y, self.value

	def return_x_y(self):
		return x,y

	def set_value(self, value):
		self.value=value	

	def set_coordinates(self, x, y):	
		self.x=x
		self.y=y

	def get_value(self):
		return self.value
