###Python soruce code for google painting problem

from line import Line
from point import Point
from square import Square

HORIZ_LEFT=60
HORIZ_RIGHT=22

VERTICAL="Vertical"
HORIZONTAL="Horizontal"

HOR=99
VER=43

VER_UP=53
VER_DOWN=34

##Function to draw a square
def paint_square(rows, columns, s):
	if(rows<1 or columns <1 or  s<1):
		print "Error"
		return -1

##Function to draw a line
def paint_line(r1, c1, r2, c2):
	if(r1<1 or c1 <1):
		print "Error"
		return -1

##Function to erase a single cell
def erease_cell(row, column):
	if(row<0 or column<0):
		print "Error"
		return -1

#Function to import the file
def import_file_painting(filename):##The file content is raw format. It is needed to parse
	content=list(open(filename))
	return content

#This function returns the number of rows and columns
def get_size_img(first_row):
	pos=first_row.find(' ')
	cols_number=first_row[pos+1:len(first_row)-1]
	rows_number=first_row[0:pos]
	return int(rows_number), int(cols_number)

##Giving in input the raw content, the function deletes the return character
def remove_return_characters(raw_content, n_cols):
	for idx, element in enumerate(raw_content):
		raw_content[idx]=element[0:n_cols-1]
	return raw_content
	
##Function to convert the strings list in a matrix of char
def list_to_matrix_char(raw_content, n_rows, n_cols):
	char_matrix=[None]*n_rows
	for idx, element in enumerate(raw_content):
		char_matrix[idx]=list(element)
	
	return char_matrix

##Function to print in pretty way the output
def print_pretty(raw_content):
	for element in raw_content:
		print element

##Is a dot function
def is_a_dot(element):
	if(element=='.'):
		return 1
	else:
		return -1

##Is a sharp function
def is_a_sharp(element):
	if(element=='#'):
		return 1
	else:
		return -1

#This function returns the subimage of the image
def get_sub_image(matrix_char, start_row, end_row, start_column, end_column):
	rows_image=matrix_char[start_row:end_row]
	sub_image=[]
	for index, element in enumerate(rows_image):
		sub_image.append(element[start_column:end_column])
	return sub_image

##This function returns the size of subimage
def get_size_sub_image(sub_image):
	n_rows=len(sub_image)
	n_cols=0
	for element in sub_image:
		n_cols=len(element)
		break
	return n_rows, n_cols

##Giving a subimage, and the mode of explore the image, this function recognizes if ???
def recognize_lines(sub_image, mode):
	rows= len(sub_image)
	cols= len(sub_image[0])
	found=False
	lines_list=[]
	starting_point=Point()
	ending_point=Point()

	if(mode==HOR):
		for i in range(0,rows):
			for j in range(0, cols):
				if(is_a_sharp(sub_image[i][j])==1 and found==False):
					starting_point=Point(j,i)
					found=True

				if (found==True and (is_a_sharp(sub_image[i][j])==-1 or j==cols-1)):
					if(j!=cols-1):
						ending_point=Point(j-1,i)
					else:
						ending_point=Point(j,i)

					recognized_line= Line(starting_point,ending_point)
					lines_list.append(recognized_line)
					found=False

		
		return lines_list

	elif(mode==VER):##To be done
		for j in range(0,cols):
			for i in range(0, rows):
				if(is_a_sharp(sub_image[i][j])==1 and found==False):
					found=True
					starting_point=Point(j,i)

				if (found==True and (is_a_sharp(sub_image[i][j])==-1 or i==rows-1)):
					if(i!=cols-1):
						ending_point=Point(j,i-1)
					else:
						ending_point=Point(j,i)

					recognized_line= Line(starting_point,ending_point)
					lines_list.append(recognized_line)
					found=False	
		
		return lines_list
	
	else:
		print "Error, choose correct mode"


##Givinf in input the  number of rows, the number of columns and a point object, this function returns the list of its neighboor.
##If the point is a boundary point the function will return -1
def get_neighboors_points(sub_image, p):
	row=p.get_y()
	col=p.get_x()
	n_rows=len(sub_image)
	n_cols=len(sub_image[0])
	neighboors_list=[]
	if(row-1<0 or col-1<0):
		return neighboors_list
	if(row+1>=n_rows or col+1>=n_cols):
		return neighboors_list

	neighboors_list.append(Point(col+1, row-1,sub_image[row-1][col+1]) )##NE
	neighboors_list.append(Point(col, row-1,sub_image[row-1][col]) )##NORTH
	neighboors_list.append(Point(col-1, row-1,sub_image[row-1][col-1]) )##NW
	neighboors_list.append(Point(col-1, row ,sub_image[row][col-1]) )##EAST
	neighboors_list.append(Point(col, row,sub_image[row][col]) )##The point
	neighboors_list.append(Point(col-1, row+1,sub_image[row+1][col-1]) )##SE
	neighboors_list.append(Point(col, row+1,sub_image[row+1][col]) )##SOUTH
	neighboors_list.append(Point(col+1, row+1,sub_image[row+1][col+1]) )##SOUTHWEST
	neighboors_list.append(Point(col+1, row,sub_image[row][col+1]) )##WEST

	return neighboors_list

##This function compares two lists. It returns -1 if either they have at least one different element or they have different lenght.
##The function returns 1 if the two lists are completely equal.
def lists_are_equal(list1, list2):
	cnt=0
	if(len(list1)!=len(list2)):
		return -1##Since they have different lenght, they can't be equal
	for i in range(len(list1)):
		if (list1[i]!=list2[i]):
			return -1
		else:
			cnt=cnt+1	
	return 1
	
def get_values_list(list_points):
	values_list=[]
	for element in list_points:
		values_list.append(element.get_value())

	return values_list

def recognize_square(sub_image, point):
	square=['#','#','#','#','#','#','#','#','#']
	neighboors_points=[]
	square_recognized=None
	list_values=[]
	
	if(is_a_sharp(sub_image[point.get_y()][point.get_x()])==1):
		neighboors_points=get_neighboors_points(sub_image, point)
		list_values=get_values_list(neighboors_points)

	if(lists_are_equal(square, list_values)==1):
		square_recognized=Square(point,1)
		
	return square_recognized	

##The image is drawn on file
def draw_image_on_file(image, filename):
	target = open(filename, 'w')
	for element in image:
		target.write(element)
		target.write("\n")
	target.close()

##Conversion frm char matrix to strings list
def char_matrix2string_list(char_matrix):
	string_list=[]
	for row in char_matrix:
		string_list.append(''.join(row))
	return string_list

def get_list_squares(sub_image):
	squares_list=[]
	n_rows_sub=len(sub_image)
	n_cols_sub=len(sub_image[0])
	for y in range(1, n_rows_sub):
		for x in range(1, n_cols_sub):
			p=Point(x,y)
			tmp_square=recognize_square(sub_image,p)
			if(tmp_square!=None):
				squares_list.append(tmp_square)
	return squares_list

def get_empty_image(n_rows, n_cols):
	empty_image=[None]*n_rows
	for x in range(0, n_rows):
		empty_image[x]=['.']*n_cols
	
	return empty_image

def get_char_matrix_from_file(filename):
	raw_content=import_file_painting(filename)
	n_rows, n_cols= get_size_img(raw_content[0])##The size is the first row.		
	raw_content.pop(0)##The first row is removed
	raw_content=remove_return_characters(raw_content, n_cols)##the return character \n are removed
	char_matrix=list_to_matrix_char(raw_content, n_rows, n_cols)##The raw conten to char matrix conversion is performed
	return char_matrix

##This function returns the lists of shapes reconginzed
def recognize_shapes(image):
	squares_list=get_list_squares(image)
	hor_lines_list=recognize_lines(image, HOR)
	ver_lines_list=recognize_lines(image, VER)
	return squares_list, hor_lines_list, ver_lines_list

def paint_square(image, square):
	print "paint square"

def draw_line(image, line):
	p1, p2=line.get_points()
	line.print_info()
	print "paint line"
	if(line.is_hor()==1):
		print "Is horizontal"

	if(line.is_ver()==1):
		print "Is vertical"

def erase_cell(image, point):
	image[point.get_y()][point.get_x()]='.'
	return image

def draw_element(image, shape):
	if(isinstance(shape, Square)==1):
		image=paint_square(image, shape)
	elif(isinstance(shape, Line)==1):
		image=draw_line(image, shape)
	elif(isinstance(shape, Point)==1):
		image=paint_square(image, Point)
	else:
		print "Insert correct shape"
	return image

def test():
	char_matrix=get_char_matrix_from_file("logo.in")
	sub_image=get_sub_image(char_matrix, 0,20,0,20)##giving the coordinates a submatrix is extracted from the char matrix
	string_list2=char_matrix2string_list(sub_image)	##Char matrix to string conversion performed in order to have a pretty print
	print_pretty(string_list2)
	squares_list, hor_lines_list, ver_lines_list= recognize_shapes(sub_image)

	empty_image=get_empty_image(len(sub_image),len(sub_image[0]))
	string_list3=char_matrix2string_list(empty_image)
	print_pretty(string_list3)

	s=squares_list[0]
	h_line=hor_lines_list[0]
	v_line=ver_lines_list[0]
	h_line.print_info()
	draw_element(empty_image, s)
	draw_element(empty_image, h_line)
	draw_element(empty_image, v_line)

test()
