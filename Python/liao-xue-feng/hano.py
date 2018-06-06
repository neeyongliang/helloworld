def Hanno(n,a,b,c):
	if n == 1:
		print a,'-->',c
		return
	Hanno(n-1,a,c,b)
	print a,'-->',c
	Hanno(n-1,b,a,c)


Hanno(4,'A','B','C')