###Python soruce code for google painting problem

from line import Line

HORIZ_LEFT=60
HORIZ_RIGHT=22

VERTICAL="Vertical"
HORIZONTAL="Horizontal"

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
def recognize_row(sub_image, mode):
	rows= len(sub_image)
	cols= len(sub_image[0])
	n_lines=0
	n_sharpes=0
	lines_list=[]

	if(mode==HORIZ_RIGHT):
		for i in range(0,rows):
			for j in range(0, cols):
				if(is_a_sharp(sub_image[i][j])==1):
					n_sharpes=n_sharpes+1

				if n_sharpes>0 and (is_a_sharp(sub_image[i][j])==-1 or j==cols-1):
					recognized_line= Line(i,j,HORIZONTAL,n_sharpes)
					lines_list.append(recognized_line)
					n_sharpes=0	
	
		return lines_list
		
	elif(mode==HORIZ_LEFT):
		print "a"

	elif(mode==VER_UP):
		print "a"

	elif(mode==VER_DOWN):
		for j in range(0,cols):
			for i in range(0, rows):
			#	print "(i,j)",i,j
				if(is_a_sharp(sub_image[i][j])==1):
					n_sharpes=n_sharpes+1

				if n_sharpes>0 and (is_a_sharp(sub_image[i][j])==-1 or j==cols-1):
					recognized_line= Line(i,j,VERTICAL,n_sharpes)
					lines_list.append(recognized_line)
					n_sharpes=0	
		
		return lines_list
	
	else:
		print "Error, choose correct mode"

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

def test():
	raw_content=import_file_painting("logo.in")	
	n_rows, n_cols= get_size_img(raw_content[0])##The size is the first row.
	raw_content.pop(0)##The first row is removed
	raw_content=remove_return_characters(raw_content, n_cols)##the return character are removed
	char_matrix=list_to_matrix_char(raw_content, n_rows, n_cols)##The raw content-char matrix conversion is performed	
	sub_image=get_sub_image(char_matrix, 0,20,0,20)##giving the coordinates a submatrix is extracted from the char matrix
	string_list2=char_matrix2string_list(sub_image)	
	print_pretty(string_list2)
	#recognize_row(sub_image, HORIZ_RIGHT)
	recognize_row(sub_image, HORIZ_RIGHT)
	
	'''
	DEBUG PRINTS
	string_list=char_matrix2string_list(sub_image)
	
	print_pretty(string_list)
	print_pretty(string_list2)
	
	'''
	
test()
