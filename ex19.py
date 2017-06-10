def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that is enough for the party!"
	print "Get a blanket\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese=25
amount_of_crackers=40

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside as well"
cheese_and_crackers(10*3, 12*3+4)

print "We can even do both as well"
cheese_and_crackers(amount_of_cheese*2, amount_of_crackers + 10)



