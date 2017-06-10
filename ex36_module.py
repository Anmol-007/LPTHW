def car_data(car):
	for data in car:
		print "%r " % data,
	print ""

def get_distance(car):
	i = car.index('Distance travelled')
	distance = car.pop(i+1)
	car.insert(i+1, distance)
	return distance

def get_fuel(car):
	i = car.index('Current Fuel')
	fuel = car.pop(i+1)
	car.insert(i+1, fuel)
	return fuel

def add_fuel(car, fuel):
	i = car.index('Current Fuel')
	old_fuel = car.pop(i+1)
	car.insert(i+1, old_fuel + fuel)
	
def drive(car, distance):
	fuel_needed = distance / 10
	current_fuel = get_fuel(car)
#	print "Fuel needed: %d, Current fuel: %d" % (fuel_needed, current_fuel)
	if fuel_needed > current_fuel:
#		print "Sorry! Insufficient fuel in tank. You can't drive %d kms" % distance
		return -1
	else:
	  	car.insert(car.index(current_fuel), car.pop(car.index(current_fuel)) - fuel_needed)
		car.insert(car.index(get_distance(car)), car.pop(car.index(get_distance(car))) + distance) 
#		print "Yeah! You just drove %d kms" % distance
		return 0
		
	
