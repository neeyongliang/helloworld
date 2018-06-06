class Person(object):
	pass
class Student(Person):
	pass
class Teather(Person):
	pass

class SkillMixin(object):
	pass
class BasketballMixin(SkillMixin):
	def skill(self):
		return 'Basketball'
class FootballMixin(SkillMixin):
	def skill(self):
		return 'Football'
class Basket_Student(BasketballMixin,Student):
	def skill(self):
		return 'Basketball Student'
class Foot_Teacher(FootballMixin,Teather):
	def skill(self):
		return 'Football Teather'

t = Foot_Teacher()
print t.skill()

s = Basket_Student()
print s.skill()
