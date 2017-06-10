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
	
son = Son()
son.multiple()

daughter = Daughter()
daughter.multiple()
