def add(a, b):
	print "ADDING %d + %d" % (a,b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a,b)
	return a-b

def multiply(a, b):
	print "MULTIPLY %d * %d" % (a,b)
	return a*b

def divide(a, b):
	print "DIVIDING %d / %d" % (a,b)
	return a/b

print "Let us do something with Math functions"

age = add(14, 9)
height = subtract(180, 7)
weight = multiply(36, 2)
iq = divide(100, 2)

print "Age: %d, Weight: %d, Height: %d, IQ: %d" % (age, weight, height, iq)

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do that by hand?"
