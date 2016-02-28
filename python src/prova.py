###Python soruce code for google painting problem
from line import Line
from point import Point
from square import Square
from parsing import *

HOR=99
VER=43

def is_a_sharp(element):
	"""Is a sharp function"""
	if(element=='#'):
		return 1
	else:
		return -1

def recognize_lines(image, mode):
	"""Giving a subimage, and the mode of explore the image, this function recognizes how many horizontal (vertical) lines are in the image"""
	rows= len(image)
	cols= len(image[0])
	found=False
	lines_list=[]
	starting_point=Point()
	ending_point=Point()

	if(mode==HOR):
		for i in range(0,rows):
			for j in range(0, cols):
				if(is_a_sharp(image[i][j])==1 and found==False):
					starting_point=Point(j,i)
					found=True

				if (found==True and (is_a_sharp(image[i][j])==-1 or j==cols-1)):
					if(j!=cols-1):
						ending_point=Point(j-1,i)
					else:
						ending_point=Point(j,i)

					recognized_line= Line(starting_point,ending_point)
					lines_list.append(recognized_line)
					found=False

		
		return lines_list

	elif(mode==VER):
		for j in range(0,cols):
			for i in range(0, rows):
				if(is_a_sharp(image[i][j])==1 and found==False):
					starting_point=Point(j,i)
					found=True

				if (found==True and (is_a_sharp(image[i][j])==-1 or i==rows-1)):
					if(i!=rows-1):##If i is not the last vertical point
						ending_point=Point(j,i-1)
					else:#If i is the last vertical point (the bottom point)
						if(is_a_sharp(image[i][j])==1):
							ending_point=Point(j,i)
						else:
							ending_point=Point(j,i-1)
					recognized_line= Line(starting_point,ending_point)
					lines_list.append(recognized_line)
					found=False	
		return lines_list
	
	else:
		print "Error, choose correct mode"

def get_coordinates(point, k):
	x=point.get_x()
	y=point.get_y()
	i=x+k
	j=y+k
	x_list=[]
	y_list=[]
	points_list=[]
	while(i>=x):
		x_list.append(i)
		y_list.append(j)
		i=i-1
		j=j-1
	i=x-k
	j=y-k
	while(i<x):
		x_list.append(i)
		y_list.append(j)		
		i=i+1
		j=j+1

	for x_el in x_list:
		for y_el in y_list:
			points_list.append(Point(x_el, y_el))
	return points_list

def get_neighboors_points(image, p, level):
	"""Giving in input an image and a point instance, this function returns the list of its neighboors. If the point is a boundary point the function will return an empty list"""
	row=p.get_y()
	col=p.get_x()
	
	n_rows=len(image)
	n_cols=len(image[0])
	neighboors_list=None

	if(row-level<0 or col-level<0):
		return neighboors_list
	if(row+level>=n_rows or col+level>=n_cols):
		return neighboors_list

	neighboors_list=get_coordinates(p, level)
	return neighboors_list

def lists_are_equal(list1, list2):
	"""This function compares two lists. It returns -1 if either they have at least one different element or they have different lenght.The function returns 1 if the two lists are completely equal."""
	if(len(list1)!=len(list2)):
		return -1##Since they have different lenght, they can't be equal
	for i in range(len(list1)):
		if (list1[i]!=list2[i]):
			return -1	
	return 1
	
def get_values_list(list_points):
	"""Given in input a points list, this function returns the values in it"""
	values_list=[]
	for element in list_points:
		values_list.append(element.get_value())

	return values_list


def are_all_sharps(image, points_list):
	"""Giving an image by which the points list is extracted, this function returns:
	 1 if all elements of points list are sharps
	-1 if less than k-1 elements are sharps
	-2 if points_list is None
	an holes_list (which is a list of Point object) if the number of sharpes are between k-2 and len(points_list)"""
	
	if(points_list==None):
		return -2
	
	cnt=0
	holes_list=[]

	for point in points_list:
		if(is_a_sharp(image[point.get_y()][point.get_x()])==1):
			cnt=cnt+1
		else:
			holes_list.append(point)
	
	if(cnt==len(points_list)):##Is a fullfilled square
		print "Fullfilled sqaure of  ",cnt, " sharps"
		return 1
	k=7
	if(cnt<k):##Is a holed square. The number of sharps is less than k.
		return -1
	
	if(cnt<len(points_list) and cnt >k):
		return holes_list	

def recognize_square(image, point):
	neighboors_points=[]
	square_recognized=None
	level=1

	if(is_a_sharp(image[point.get_y()][point.get_x()])==1):
		neighboors_points=get_neighboors_points(image, point,level)
		
		if(are_all_sharps(image, neighboors_points)==-1):
			square_recognized=Square(point,0)
			return square_recognized

		tmp=are_all_sharps(image, neighboors_points)
		print type(tmp)
		if(isinstance(tmp,list)==1):
			square_recognized=Square(point,1,tmp)

		while(are_all_sharps(image, neighboors_points)==1):		
			level=level+1
			neighboors_points=get_neighboors_points(image, point,level)
			
		square_recognized=Square(point,level-1, neighboors_points)
		return square_recognized

def recognize_squares(image):
	"""This function returns the squares list in the image"""
	squares_list=[]
	n_rows_sub=len(image)
	n_cols_sub=len(image[0])
	for y in range(0, n_rows_sub):
		for x in range(0, n_cols_sub):
			p=Point(x,y)
			tmp_square=recognize_square(image,p)
			if(tmp_square!=None):
				squares_list.append(tmp_square)
	return squares_list

def recognize_shapes(image):
	"""This function returns the lists of shapes reconginzed"""
	squares_list=recognize_squares(image)
	hor_lines_list=recognize_lines(image, HOR)
	ver_lines_list=recognize_lines(image, VER)
	return squares_list, hor_lines_list, ver_lines_list

def draw_square(image, square):
	"""This function draws a square in the image. It returns the drawn image"""

	center=square.get_center()
	neighboor_points=get_neighboors_points(image, center, square.get_radius())
	print "PAINT_SQUARE", center.get_x(), center.get_y(), "(r:",square.get_radius(),")"
	for point in neighboor_points:
		image[point.get_y()][point.get_x()]='#'
	return image		

def draw_line(image, line):
	"""This function draws a line in the image. It returns the drawn image"""
	if(line.is_hor()==1):
		p1, p2=line.get_points()
		print "PAINT_H_LINE", p1.get_x(),  p1.get_y(), p2.get_x(),  p2.get_y(), "( L:",line.get_lenght(),")"
		for i in range(p1.get_x(), p2.get_x()+1):
			image[p1.get_y()][i]='#'	
		return image

	if(line.is_ver()==1):
		p1, p2=line.get_points()
		print "PAINT_V_LINE", p1.get_x(),  p1.get_y(), p2.get_x(),  p2.get_y(), "( L:",line.get_lenght(),")"
		for i in range(p1.get_y(), p2.get_y()+1):
			image[i][p1.get_x()]='#'
		return image

def erase_cell(image, point):
	"""This function erase in the image. It returns the image with erased cell"""
	image[point.get_y()][point.get_x()]='.'
	print "ERASE_CELL", point.get_x(), point.get_y()
	return image

def draw_element(image, shape):
	if(isinstance(shape, Square)==1):
		image=draw_square(image, shape)
	elif(isinstance(shape, Line)==1):
		image=draw_line(image, shape)
	elif(isinstance(shape, Point)==1):
		image=paint_square(image, Point)
	else:
		print "Insert correct shape"
	return image

def print_image(char_matrix):
	""" Giving in input a char matrix, this function prints the corresponding image, perforing, before the print, a char-matrix2strings-list conversion"""
	strings_list=char_matrix2string_list(char_matrix)
	print_pretty(strings_list)

def get_greatest_shapes(shapes_list, fraction=1):
	max_elements=int(len(shapes_list)*fraction)

	#print "max_elements:", max_elements
	if(fraction<0 or fraction >1):
		print "Fraction must be between 0 and 1"
		return -1
	if(isinstance(shapes_list[0], Square)==1):
		max_radius=0
		for square in shapes_list:
			radius=square.get_radius()
			if(radius>max_radius):
				biggest_square=square
				max_radius=radius
		return biggest_square
	
	if(isinstance(shapes_list[0], Line)==1):
		max_length=0
		for line in shapes_list:
			length=line.get_lenght()
			if(length>max_length):
				longest_line=line
				max_length=length
		return longest_line
	

def draw_image_by(image, chose):
	squares_list, hor_lines_list, ver_lines_list= recognize_shapes(image)
	print_image(image)
	empty_image=get_empty_image(len(image),len(image[0]))
	#print_image(empty_image)
	print "\n"
	if(chose==1):
		for s in squares_list:
			empty_image=draw_element(empty_image,s)
	if(chose==2):
		for h in  hor_lines_list:
			empty_image=draw_element(empty_image,h)
	if(chose==3):	
		for v in  ver_lines_list:
			empty_image=draw_element(empty_image,v)
	
	
	print_image(empty_image)
	return empty_image

def draw_biggest_square(image, squares_list):
	biggest_square=get_greatest_shapes(squares_list)
	image=draw_square(image, biggest_square)
	print_image(image)
	return image

def draw_longest_line(image, lines_list):
	longest_line=get_greatest_shapes(lines_list)
	image=draw_line(image, longest_line)
	print_image(image)
	return image

def count_sharps(image):
	count=0
	for y in range(0, len(image)):
		for x in range(0, len(image[0])):
			if(is_a_sharp(image[y][x])==1):
				count=count+1
	return count

def how_much_filled(image, drawn_image):
	total=float(count_sharps(image))
	partial=float(count_sharps( drawn_image))
	fraction=float(partial/total)
	return fraction

def are_equal(image1, image2):
	if(image1==None or image2==None):
		print "The images must not be none"

	if(len(image1)!=len(image2)):
		print "Different length"
		return -1

	for y in range (0, len(image1)):
		for x in range(0, len(image1[0])):
			if(image1[y][x]!=image2[y][x]):
				print "Element different at (row, column)", y,x
				return -1
	print "They are equal"	
	return 1
		

def test():
	image=get_char_matrix_from_file("logo.in")
	squares_list, hor_lines_list, ver_lines_list= recognize_shapes(image)
	print_image(image)
	'''
	empty_image=draw_longest_line(empty_image, ver_lines_list)	
	print how_much_filled(image, empty_image)
	empty_image=draw_longest_line(empty_image, hor_lines_list)
	print how_much_filled(image, empty_image)
	empty_image=draw_biggest_square(empty_image, squares_list)
	print how_much_filled(image, empty_image)
	'''
test()
