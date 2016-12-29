from sys import argv
script,input_file = argv

def print_call(f):
	print f.read()

def rewind(f):
	f.seek(0)
	#seek() 函数的处理对象是 字节 而非行，所以 seek(0) 只是转到文件的 0 byte，也就是第一个 byte 的位置。

def print_a_line(line_count,f):
	print line_count,f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"
print print_call(current_file)
print "Now let's rewind,kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line,current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)