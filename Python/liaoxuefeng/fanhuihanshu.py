def calc_prod(lst):
	def dely_prod():
		def f(x,y):
			return x*y
		return reduce(f,lst,1)
	return dely_prod
f = calc_prod([1,3,5,7])
print f()