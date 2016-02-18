VERTICAL="Vertical"
HORIZONTAL="Horizontal"
DEFAULT=-1

class Line:
	r1=DEFAULT
	r2=DEFAULT
	c1=DEFAULT
	c2=DEFAULT

	def __init__(self, r1, c1, r2, c2):
		self.r1=r1
		self.c1=c1
		self.r2=r2
		self.c2=c2

	##Actually the returned values is not still correvt beacuse it doesn't take into account the last element. TO FIX
	def get_lenght(self):
		if(self.c1==self.c2):
			return (self.r2-self.r1)
		if(self.r1==self.r2):
			return (self.c2-self.c1)


	def printInfo(self):
		print "(r1,c1)", self.r1, self.c1
		print "(r2,c2)", self.r2, self.c2
		#print "Len: ", self.get_lenght()


