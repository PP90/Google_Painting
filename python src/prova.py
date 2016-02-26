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
					if(i!=rows-1):
						ending_point=Point(j,i-1)
					else:
						ending_point=Point(j,i)

					recognized_line= Line(starting_point,ending_point)
					lines_list.append(recognized_line)
					found=False	
		
		return lines_list
	
	else:
		print "Error, choose correct mode"


def get_neighboors_points(image, p, level=1):
	"""Giving in input an image and a point instance, this function returns the list of its neighboors. If the point is a boundary point the function will return -1"""
	row=p.get_y()
	col=p.get_x()
	
	n_rows=len(image)
	n_cols=len(image[0])
	neighboors_list=[]

	if(row-level<0 or col-level<0):
		return neighboors_list
	if(row+level>=n_rows or col+level>=n_cols):
		return neighboors_list

	##This function has to be generalized for square ok k radius (k>1)
	neighboors_list.append(Point(col+1, row-1,image[row-1][col+1]) )##NE
	neighboors_list.append(Point(col, row-1,image[row-1][col]) )##NORTH
	neighboors_list.append(Point(col-1, row-1,image[row-1][col-1]) )##NW
	neighboors_list.append(Point(col-1, row ,image[row][col-1]) )##EAST
	neighboors_list.append(Point(col, row,image[row][col]) )##The point
	neighboors_list.append(Point(col-1, row+1,image[row+1][col-1]) )##SE
	neighboors_list.append(Point(col, row+1,image[row+1][col]) )##SOUTH
	neighboors_list.append(Point(col+1, row+1,image[row+1][col+1]) )##SOUTHWEST
	neighboors_list.append(Point(col+1, row,image[row][col+1]) )##WEST

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

def recognize_square(image, point):##Actually this function has to be generalized for square which radius has to be bigger than 1
	square=['#','#','#','#','#','#','#','#','#']
	neighboors_points=[]
	square_recognized=None
	list_values=[]
	
	if(is_a_sharp(image[point.get_y()][point.get_x()])==1):
		neighboors_points=get_neighboors_points(image, point)
		list_values=get_values_list(neighboors_points)

		if(lists_are_equal(square, list_values)==1):
			square_recognized=Square(point,1)
		else:
			square_recognized=Square(point,0)
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
	
	return empty_image

def recognize_shapes(image):
	"""This function returns the lists of shapes reconginzed"""
	squares_list=recognize_squares(image)
	hor_lines_list=recognize_lines(image, HOR)
	ver_lines_list=recognize_lines(image, VER)
	return squares_list, hor_lines_list, ver_lines_list

def draw_square(image, square):
	"""This function draws a square in the image. It returns the drawn image"""
	if(square.get_radius()==1):
		center=square.get_center()
		neighboor_points=get_neighboors_points(image, center)
		print "PAINT_SQUARE", center.get_x(), center.get_y(), "(r:",square.get_radius(),")"
		for point in neighboor_points:
			image[point.get_y()][point.get_x()]='#'
	return image		

def draw_line(image, line):
	"""This function draws a line in the image. It returns the drawn image"""
	if(line.is_hor()==1):
		p1, p2=line.get_points()
		print "PAINT_LINE", p1.get_x(),  p1.get_y(), p2.get_x(),  p2.get_y(), "( l:",line.get_lenght(),")"
		for i in range(p1.get_x(), p2.get_x()+1):
			image[p1.get_y()][i]='#'
			
		return image

	if(line.is_ver()==1):
		p1, p2=line.get_points()
		print "PAINT_LINE", p1.get_x(),  p1.get_y(), p2.get_x(),  p2.get_y(), "( l:",line.get_lenght(),")"
		for i in range(p1.get_y(), p2.get_y()+1):
			image[i][p1.get_x()]='#'
		return image

def erase_cell(image, point):
	"""This function erase in the image. It returns the image with erased cell"""
	image[point.get_y()][point.get_x()]='.'
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

def test():
	image=get_char_matrix_from_file("logo.in")
	print_image(image)
	squares_list, hor_lines_list, ver_lines_list= recognize_shapes(image)
	print "\n"
	empty_image=get_empty_image(len(image),len(image[0]))
	print_image(empty_image)
	print "\n"

	#for s in squares_list:
	#	empty_image=draw_element(empty_image,s)
	
	
	#for h in  hor_lines_list:
	#	empty_image=draw_element(empty_image,h)
		
	for v in  ver_lines_list:
		empty_image=draw_element(empty_image,v)
	print_image(empty_image)
	
	
test()
