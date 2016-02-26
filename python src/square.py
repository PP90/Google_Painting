from point import Point
DEFAULT=-1
class Square:
	center=DEFAULT
	radius=DEFAULT

	def __init__(self, center, radius):
		self.center=center
		self.radius=radius

	def print_info(self):
		self.center.print_info()
		print "rad: ", self.radius
	
	def get_radius(self):
		return self.radius

	def get_center(self):
		return self.center


	def get_points_list(self):
		print "to implement"
