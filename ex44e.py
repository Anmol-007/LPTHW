class Dad(object):
	
	def multiple(self):
		print "Hello, I am your Dad:)"

class Mom(object):
	
	def multiple(self):
		print "Hello, I am your Mom:)"

class Son(Mom, Dad):
	
	def multiple(self):
		print "Hello, I am your Son:)"
		super(Son, self).multiple()

class Daughter(Dad, Mom):
	
	def multiple(self):
		print "Hello, I am your Daughter:)"
		super(Daughter, self).multiple()
	
#son = Son()
#son.multiple()
#
#daughter = Daughter()
#daughter.multiple()

class Other(object):
	
	def overide(self):
		print "OTHER overide()"
	
	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class Child(object):
	
	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def overide(self):
		print "CHILD overide()"

	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"

child = Child()
child.implicit()
child.overide()
child.altered()
