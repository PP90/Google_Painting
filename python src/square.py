from point import Point
DEFAULT=-1
class Square:
	center=DEFAULT
	radius=DEFAULT
	holes_points=DEFAULT
	neighboors_points=DEFAULT

	def __init__(self, center, radius, neighboors_points=None, holes_points=None):
		self.center=center
		self.radius=radius
		self.holes_points=holes_points
		self.neighboors_points=neighboors_points

	def print_info(self):
		self.center.print_info()
		print "R: ", self.radius
		if(self.neighboors_points!=None):
			print "Neighboors list:"
			for point in self.neighboors_points:
				point.print_info()
	
	def get_radius(self):
		return self.radius

	def get_center(self):
		return self.center

	def get_neighboor_points(self):
		self.neighboors_points

