
class Thing(object):

	def __init__(self, name):
		self.name = name

a = [1, 12, 43, 65, 3]
b = [32, 67, 98, 12]
c = []

for num1 in a:
	for num2 in b:
		if num1 == num2:
			print "%d at %d in a is equal to %d in at %d of b." % (num1, a.index(num1), num2, b.index(num2))

