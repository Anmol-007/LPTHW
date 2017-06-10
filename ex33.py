def create_list(num, increment):
	i = 0	
	numbers = []

	while i < num:
		#print "At the top i = %d." % i
		numbers.append(i)

		i += increment
		#print "Numbers now: ", numbers

		#print "At the bottom i = %d." % i

	print "The numbers: ", numbers
	return numbers
		
for i in create_list(25, 2):
	print i
