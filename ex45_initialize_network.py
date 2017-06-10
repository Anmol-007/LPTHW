from ex45_trainsystem import *

print "Initializing network..."
western = TrainLine("Western", 40)
western_stations = ["Borivali", "Kandivali", "Goregaon", "Malad", "Ram Mandir", 
		"Jogeshwari", "Andheri", "Vile Parle", "Santacruz", "Khar Road", "Bandra"]
western_distances = {"Borivali":0, "Kandivali":3, "Malad":6, "Goregaon":8, 
		"Ram Mandir":10, "Jogeshwari":12, "Andheri":15, 
		"Vile Parle":17, "Santacruz":19, "Khar Road":21, "Bandra":23}

western.create_line(western_stations, western_distances)
western.show_stations()	

#western_line = western.get_stations()
#
#print "Western Line stations"
#for station in western_line:
#	print station.name + "(%d)" % station.distance,
#
central = TrainLine("Central", 45)
central_stations = ["Thane", "Mulund", "Nahur", "Bhandup", "Kanjur Marg", 
		"Vikhroli", "Ghatkopar", "Vidyavihar", "Kurla"]
central_distances = {"Thane":0, "Mulund":4, "Nahur":6, "Bhandup":8, 
		"Kanjur Marg":10, "Vikhroli":12, "Ghatkopar":15, 
		"Vidyavihar":17, "Kurla":20}

central.create_line(central_stations, central_distances)
central.show_stations()

metro1 = TrainLine("Metro 1", 50)
metro1_stations = ["Versova", "D N Nagar", "Azad Nagar", "Andheri", 
		"Western Express Highway", "Chakala", "Airport Road", 
		"Marol Naka", "Saki Naka", "Asalpha", "Jagruti Nagar", "Ghatkopar"]
metro1_distances = {"Versova":0, "D N Nagar":1, "Azad Nagar":2, "Andheri":3, 
		"Western Express Highway":4, "Chakala":5, "Airport Road":6,
		"Marol Naka":7, "Saki Naka":8, "Asalpha":9, "Jagruti Nagar":10,
		"Ghatkopar":11}

metro1.create_line(metro1_stations, metro1_distances)
metro1.show_stations()

mumbai.get_trip("Borivali", "Jogeshwari
