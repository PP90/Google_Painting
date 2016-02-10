###Python soruce code for google painting problem

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

def get_size_img(raw_content):
	first_row=raw_content[0]
	pos=first_row.find(' ')
	cols_number=first_row[pos+1:len(first_row)-1]
	rows_number=first_row[0:pos]
	return int(rows_number), int(cols_number)

def test():
	raw_content=import_file_painting("logo.in")	
	get_size_img(raw_content)

test()
