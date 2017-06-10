the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
#This is a mixed list containing integers and strings
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first for-loop goes through a list

for number in the_count:
	print "This is count %d." % number

for fruit in fruits:
	print "The fruit is %s." % fruit

#We can go through mixed lists too
for i in change:
	print "I got %r" % i

#we can also build lists, starting from an empty one
elements = []

elements.extend(range(1,8))
#for i in range(0,7):
#	print "Adding %d to list 'elements'." % i
#	#append is the function used to add items to aa list
#	elements.append(i)

for item in elements:
	print "Item is: %d." % item

