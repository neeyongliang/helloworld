from sys import argv
script,filename = argv
txt = open(filename)
print "Here's you file %r:"%filename
print txt.read()

print "Here is filename %r:"%filename
print "type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)
print txt_again.read()