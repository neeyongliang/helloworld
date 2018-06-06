def is_not_empty(s):
	return s and len(s.strip()) > 0

print filter(is_not_empty,['test',None,'','str','  ','END'])