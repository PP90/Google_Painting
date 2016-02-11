###Python soruce code for google painting problem

HORIZ_LEFT=60
HORIZ_RIGHT=22

VER_UP=53
VER_DOWN=34

def paint_square(rows, columns, s):
	if(rows<1 or columns <1 or  s<1):
		print "Error"
		return -1

def paint_line(r1, c1, r2, c2):
	if(r1<1 or c1 <1):
		print "Error"
		return -1

def erease_cell(row, column):
	if(row<0 or column<0):
		print "Error"
		return -1

def import_file_painting(filename):##The file content is raw format. It is needed to parse
	content=list(open(filename))
	return content

def get_size_img(first_row):
	pos=first_row.find(' ')
	cols_number=first_row[pos+1:len(first_row)-1]
	rows_number=first_row[0:pos]
	return int(rows_number), int(cols_number)

def remove_return_characters(raw_content, n_cols):
	for idx, element in enumerate(raw_content):
		raw_content[idx]=element[0:n_cols-1]
	return raw_content
	
def list_to_matrix_char(raw_content, n_rows, n_cols):
	char_matrix=[None]*n_rows
	for idx, element in enumerate(raw_content):
		char_matrix[idx]=list(element)
	
	return char_matrix

def print_pretty(raw_content):
	for element in raw_content:
		print element

def is_a_dot(element):
	if(element=='.'):
		return 1
	else:
		return -1

def is_a_sharp(element):
	if(element=='#'):
		return 1
	else:
		return -1

def get_sub_image(matrix_char, start_row, end_row, start_column, end_column):
	rows_image=matrix_char[start_row:end_row]
	sub_image=[]
	for index, element in enumerate(rows_image):
		sub_image.append(element[start_column:end_column])
	return sub_image

def get_size_sub_image(sub_image):
	n_rows=len(sub_image)
	n_cols=0
	for element in sub_image:
		n_cols=len(element)
		break
	return n_rows, n_cols

def recognize_row(sub_image, mode):
		print "cacca"

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
	print get_size_sub_image(sub_image)

	
	'''
	DEBUG PRINTS
	string_list=char_matrix2string_list(sub_image)
	string_list2=char_matrix2string_list(char_matrix)
	print_pretty(string_list)
	print_pretty(string_list2)
	#print_pretty(sub_image)
	'''
	
test()
