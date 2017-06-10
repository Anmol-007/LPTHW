from ex45_trainsystem import *

all_stations = {} #dictionary of all stations {stationName (String) : station (Object)}
#
#Creating Western line
#
western = TrainLine("Western", 40.00)
western_station_names = ["Borivali", "Kandivali", "Goregaon", "Malad", "Ram Mandir", 
		"Jogeshwari", "Andheri", "Vile Parle", "Santacruz", "Khar Road", "Bandra"]

western_distances = {
		"Borivali"	:	0, 
		"Kandivali"	:	3, 
		"Malad"		:	6, 
		"Goregaon"	:	8, 
		"Ram Mandir"	:	10, 
		"Jogeshwari"	:	12, 
		"Andheri"	:	15, 
		"Vile Parle"	:	17, 
		"Santacruz"	:	19, 
		"Khar Road"	:	21, 
		"Bandra"	:	23
		}

western_stations = [] #list of stations on western line

for stationName in western_station_names:
	isStation = False
	newStation, isStation = is_station(all_stations, stationName)
	if isStation:
		newStation.set_change_station()
		western_stations.append(newStation)
	else:
		newStation = Station(stationName, western_distances[stationName])
		western_stations.append(newStation)
		all_stations[stationName] = newStation

western.create_line(western_stations)
#western.show_stations()	


central = TrainLine("Central", 45.00)
central_station_names = ["Thane", "Mulund", "Nahur", "Bhandup", "Kanjur Marg", 
		"Vikhroli", "Ghatkopar", "Vidyavihar", "Kurla"]
central_distances = {
		"Thane"		:	0, 
		"Mulund"	:	4, 
		"Nahur"		:	6, 
		"Bhandup"	:	8, 
		"Kanjur Marg"	:	10, 
		"Vikhroli"	:	12, 
		"Ghatkopar"	:	15, 
		"Vidyavihar"	:	17, 
		"Kurla"		:	20
		}
central_stations = []
for stationName in central_station_names:
	isStation = False
	newStation, isStation = is_station(all_stations, stationName)
	if isStation:
		newStation.set_change_station()
		central_stations.append(newStation)
	else:
		newStation = Station(stationName, central_distances[stationName])
		central_stations.append(newStation)
		all_stations[stationName] = newStation

central.create_line(central_stations)
#central.show_stations()

metro1 = TrainLine("Metro 1", 50.00)
metro1_station_names = ["Versova", "D N Nagar", "Azad Nagar", "Andheri", 
		"Western Express Highway", "Chakala", "Airport Road", 
		"Marol Naka", "Saki Naka", "Asalpha", "Jagruti Nagar", "Ghatkopar"]
metro1_distances = {
		"Versova"	:  	0, 
		"D N Nagar" 	: 	1, 
		"Azad Nagar" 	:	2, 
		"Andheri"	:	3, 
		"Western Express Highway":	4, 
		"Chakala"	:	5, 
		"Airport Road"	:	6,
		"Marol Naka"	:	7, 
		"Saki Naka"	:	8, 
		"Asalpha"	:	9, 
		"Jagruti Nagar"	:	10,
		"Ghatkopar"	:	11
		}
metro1_stations = []
for stationName in metro1_station_names:
	newStation, isStation = is_station(all_stations, stationName)
	if isStation:
		newStation.set_change_station()
		metro1_stations.append(newStation)
	else:
		newStation = Station(stationName, metro1_distances[stationName])
		metro1_stations.append(newStation)
		all_stations[stationName] = newStation

metro1.create_line(metro1_stations)
#metro1.show_stations()
#lines = []
#lines.append(western)
#lines.append(central)
#lines.append(metro1)
mumbai = TrainNetwork("Mumbai")
#print mumbai.get_name()
mumbai.build_network([western, central, metro1])
mumbai.show_lines()
stationExists, andheri = mumbai.get_station("Andheri")
stationExists, ghatkopar = mumbai.get_station("Ghatkopar")
stationExists, borivli = mumbai.get_station("Borivali");
#station.show_lines()
