DEFAULT=-1

class Point:
	x=DEFAULT
	y=DEFAULT
	

	def __init__(self, x=DEFAULT, y=DEFAULT):
		self.x=x		
		self.y=y
		
	def get_y(self):
		return self.y

	def get_x(self):
		return self.x

	def print_info(self):
		print "(x,y)", self.x, self.y

	def return_x_y(self):
		return x,y

	def set_values(self, x, y):	
		self.x=x
		self.y=y
