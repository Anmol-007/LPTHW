ten_things = "Apples Oranges Mangoes Pineapples Grapes Guava"

print "Wait, those don't add to ten", ten_things

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Banana", "Corn", "Girl", "Boy"]

while len(stuff) != 10:
	next = more_stuff.pop()
	print "Adding: ", next
	stuff.append(next)
	print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let us do some more interesting stuff with 'stuff'"

print stuff[1]
print stuff[-1]
print stuff
print stuff.pop()
print ' '.join(stuff)
print '*'.join(stuff[2:5])

