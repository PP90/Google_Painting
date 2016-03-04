from point import Point
DEFAULT=-1
class Square:
	center=DEFAULT
	radius=DEFAULT
	holes_points=DEFAULT
	points=DEFAULT

	def __init__(self, center, radius, points=None, holes_points=None):
		self.center=center
		self.radius=radius
		self.holes_points=holes_points
		self.points=points
		

	def print_info(self):
		print "Center:"
		self.center.print_info()
		print "R: ", self.radius
		if(self.points!=None):
			print "Points:"
			for point in self.points:
				point.print_info()
		if(self.holes_points!=None):
			print "Holes list:"
			for point in self.holes_points:
				point.print_info()
	
	def get_radius(self):
		return self.radius

	def get_center(self):
		return self.center

	def get_points(self):
		return self.points

	def get_holes_points(self):
		return self.holes_points

	def get_size(self):##To be generalized. Now is fittizzio assai tanto per farlo funzionare
		if(isinstance(self.points,list)==1):
			if(self.radius==1):
				return 9
			if(self.radius==2):
				return 25
		else:
			return 1
