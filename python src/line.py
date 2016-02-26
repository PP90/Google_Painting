from point import Point

class Line:
	point_p1=DEFAULT
	point_p2=DEFAULT

	def __init__(self, point_p1, point_p2):
		self.point_p1=point_p1
		self.point_p2=point_p2

	def get_lenght(self):
		if(self.point_p1.get_x()==self.point_p2.get_x()):
			return (self.point_p2.get_y()-self.point_p1.get_y()+1)
		if(self.point_p1.get_y()==self.point_p2.get_y()):
			return (self.point_p2.get_x()-self.point_p1.get_x()+1)


	def print_info(self):
		self.point_p1.print_info()
		self.point_p2.print_info()
		print self.get_lenght()

	def is_hor(self):
		if(self.point_p1.get_y()==self.point_p2.get_y()):
			return 1

	def is_ver(self):
		if(self.point_p1.get_x()==self.point_p2.get_x()):
			return 1

	def get_points(self):
		return self.point_p1, self.point_p2



