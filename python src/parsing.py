##List of function used for import image from the file and parse the image in correct way
###Python soruce code for google painting problem
from line import Line
from point import Point
from square import Square

def import_file_painting(filename):
	"""Function to import the file as strings list"""
	content=list(open(filename))
	return content

def get_size_img(first_row):
	"""This function returns the number of rows and columns of the image"""
	pos=first_row.find(' ')
	cols_number=first_row[pos+1:len(first_row)-1]
	rows_number=first_row[0:pos]
	return int(rows_number), int(cols_number)

def remove_return_characters(raw_content, n_cols):
	"""Giving in input the raw content, the function removes the return character"""
	for idx, element in enumerate(raw_content):
		raw_content[idx]=element[0:n_cols-1]
	return raw_content
	
def list_to_matrix_char(raw_content, n_rows, n_cols):
	"""Function to convert from strings list to a matrix of char"""
	char_matrix=[None]*n_rows
	for idx, element in enumerate(raw_content):
		char_matrix[idx]=list(element)
	
	return char_matrix

def print_pretty(raw_content):
	"""Function to print in pretty way the output"""
	for element in raw_content:
		print element

def get_sub_image(matrix_char, start_row, end_row, start_column, end_column):
	"""This function returns a subimage of an image"""
	rows_image=matrix_char[start_row:end_row]
	sub_image=[]
	for index, element in enumerate(rows_image):
		sub_image.append(element[start_column:end_column])
	return sub_image

def draw_image_on_file(image, filename):
	"""The image is drawn on file"""
	target = open(filename, 'w')
	for element in image:
		target.write(element)
		target.write("\n")
	target.close()

def char_matrix2string_list(char_matrix):
	"""Conversion from char matrix to strings list"""
	string_list=[]
	for row in char_matrix:
		string_list.append(''.join(row))
	return string_list

def get_empty_image(n_rows, n_cols):
	"""An empty image is created. Empty means that the image is matrix of n_rows x n_cols elements"""
	empty_image=[None]*n_rows
	for x in range(0, n_rows):
		empty_image[x]=['.']*n_cols
	
	return empty_image

def get_char_matrix_from_file(filename):
	"""Giving in input the file name, this function returns a char matrix"""
	raw_content=import_file_painting(filename)
	n_rows, n_cols= get_size_img(raw_content[0])##The size is the first row.		
	raw_content.pop(0)##The first row is removed
	raw_content=remove_return_characters(raw_content, n_cols)##the return character \n are removed
	char_matrix=list_to_matrix_char(raw_content, n_rows, n_cols)##The raw content (list of strings) to char matrix conversion is performed
	return char_matrix

