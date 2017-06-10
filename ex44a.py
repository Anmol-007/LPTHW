class Parent(object):
	
	def implicit(self):
		print "PARENT implicit()"

class Child(Parent):
	pass

mom = Parent()
son = Child()

mom.implicit()
son.implicit()	
