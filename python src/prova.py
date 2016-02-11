###Python soruce code for google painting problem

HORIZONTAL_WAY=60
VERTICAL_WAY=22
UP=12
DOWN=34

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

def get_sub_image(image, hor_size, ver_size):
	print "to do"


def get_size_sub_image(sub_image):
	print "to do"

def recognize_row(sub_image, mode):
		print "to do"

def test():
	raw_content=import_file_painting("logo.in")	
	n_rows, n_cols= get_size_img(raw_content[0])
	raw_content.pop(0)
	raw_content=remove_return_characters(raw_content, n_cols)	
	char_matrix=list_to_matrix_char(raw_content, n_rows, n_cols)
	print_pretty(raw_content)

	
test()
