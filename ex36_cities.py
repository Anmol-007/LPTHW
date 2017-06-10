from ex36_module import *
from random import *

def to_pune(car):
	distance = 120
	if drive(car, distance) == 0:
		print "Welcome to Pune, the cultural capital of Maharashtra."
		print "You have two options:"
		print "1. Refuel your car with 12 litres of fuel"
		print "2. Refuel your car with random quantity of fuel ranging from 6 to 36 litres."
		
		choice = False
		while not choice:
			next = raw_input("Which option do you choose? 1 or 2> ")		
			if next == "1":
				add_fuel(car, 12)
				car_data(car)
				choice = True
			elif next == "2":
				add_fuel(car, randint(6, 36))
				car_data(car)
				choice = True
			else:
				print "Please choose between options 1 and 2"
		go_home(car, 120)						
	else:
		print "\nYou do not have sufficient fuel to go to Pune. Please choose another destination"
		car_data(car)
		choose_destination(car)

def to_goa(car):
	distance = 600
	if drive(car, distance) == 0:
		print "Welcome to Goa. Ready to party?"
		print "You have two options:"
		print "1. Refuel your car with 50 litres of fuel"
		print "2. Refuel your car with random quantity of fuel ranging from 30 to 70 litres."
		
		choice = False
		while not choice:
			next = raw_input("Which option do you choose? 1 or 2> ")		
			if next == "1":
				add_fuel(car, 50)
				car_data(car)
				choice = True
			elif next == "2":
				add_fuel(car, randint(30, 70))
				car_data(car)
				choice = True
			else:
				print "Please choose between options 1 and 2"						
		go_home(car, 600)
	else:
		print "\nYou do not have sufficient fuel to go to Goa. Please choose another destination"
		car_data(car)
		choose_destination(car)

def go_home(car, distance):
	if drive(car, distance) == 0:
		print "\nYaa! We're going to Mumbai. Home sweet home! You have reached home safely."
			
		choice = False
		while not choice:	
			print "Do you wish to visit another city?"
			next = raw_input("Y or N?> ")
			if next == "Y":
				choice = True
				choose_destination(car)
			elif next == "N":
				choice = True
				print "You have finished your game. Your score is %d" % get_distance(car)	
	else:
		print "\nYou do not have sufficient fuel to go home!"
		print "You are stuck!"
		print "GAME OVER!!!"
		

def choose_destination(car):
	print "Please choose a destination: \n1. Pune\n2. Goa\n3. End game"
	choice = False
	while not choice:
		next = raw_input("> ")
		if next == "Pune":
			choice = True
			to_pune(car)
		elif next == "Goa":
			choice = True
			to_goa(car)
		elif next == "End Game":
			choice = True
			print "You have finished your game. Your score is %d" % get_distance(car)	
		else: 
			print "Please enter either 'Pune' or 'Goa'"
def start_game():
	car = ['Distance travelled', 0, 'Current Fuel', 0]
	add_fuel(car, 100)
	choose_destination(car)

start_game()
