class Person(object):
	def __init__(self,name,gender):
		self.name = name
		self.gender = gender
class Student(Person):
	def __init__(self, name,gender,score):
		super(Student,self).__init__(name,gender)
		self.score = score
	def __str__(self):
		return ('Student:name is %s,gender is %s,score is %s')%(self.name,self.gender,self.score)
	__repr__ = __str__

p = Student('Bob','male',88)
print p