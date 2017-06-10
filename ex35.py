from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Please type number 0 or 1")
	if how_much < 50:
		print "Nice, you're not greedy, you Win!"
		exit(0)
	else:
		dead("You are greedy. You do not deserve wealth. You lose!")
	
def bear_room():
	print "There is a giant bear here."
	print "The bear has a lot of honey."
	print "Ther bear is sitting in forn of another door."
	print "How do you move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input("> ")
		
		if next == "take honey":
			dead("The bear looks at you and slaps your face off")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets angry and attacks you. You lose!")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "Please either 'take honey' or taunt bear' or 'open door'."

def monster_room():
	print "Here you meet the great devil monster."
	print "It stares at you."
	print "Do you flee for your life or attack him?"
	
	next = raw_input("> ")
	
	if "flee" in next:
		start()
	elif "attack" in next:
		print "You are brave. You win!"
	else:
		monster_room()

def dead(why):
	print why, "Try again!"
	exit(0)

def start():
	print "You are in a dark room."
	print "There is a door to your left and one to your right."
	print "Which one do you take?"
	
	next = raw_input("> ")

	if next == "left":
		bear_room()
	elif next == "right":
		monster_room()
	else:
		dead("You drown in the darkness. You lose!")

start()
