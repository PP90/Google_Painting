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
	f=list(open(filename))
	return content

def parse_imported_file(raw_content):
	

def test():
	raw_content=import_file_painting("logo.in")	
	print raw_content

test()
