print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door =  raw_input("> ")

if door == "1":
	print "There's a giant Panda eating Velchi bananas and Alphanso mangoes. What do you do?"
	print "1. Take the Alphanso mangoes."
	print "2. Take the Velchi bananas."
	
	panda = raw_input("> ")
	
	if panda == "1":
		print "The Panda asks for Gems candy in return."
		print "1. You give him the candy."
		print "2. You decline the offer."
		
		gems = raw_input("> ")

		if gems == "1":
			print "Panda gives you the Alphanso mangoes. You both are happy. You Win!"
		elif gems == "2":
			print "Panda uses Kungu-Fu to teach you a lesson."
		else:
			print "Panda gets angry!"
	elif panda == "2":
		print "The Panda asks for Frooti in return."
		print "1. You give him the Frooti."
		print "2. You decline the offer."
		
		gems = raw_input("> ")

		if gems == "1":
			print "Panda gives you the Velchi bananas. You both are happy. You Win!"
		elif gems == "2":
			print "Panda uses Kungu-Fu to teach you a lesson."
		else:
			print "Panda gets angry!"
	else:
		print "The Panda throws you out of the room :P"
	
elif door == "2":
	print "There is a dragon sleeping on a giant pile of gold. What do you do?"
	print "1. Grab a small quantity of gold without waking the dragon."
	print "2. Yell at the dragon to make him move so you can take all the gold."

	dragon = raw_input("> ")
	
	if dragon == "1":
		print "You become wealthy! Congratulations! You Win! :)"
	elif dragon == "2":
		print "You are greedy. The dragon burns you to crisp!"
	else:
		print "You're an indecisive loser. You get no gold!"
else:
	print "The Panda and the Dragon come out of the door. You better run! \n You get nothing \n You're still a loser :P."
