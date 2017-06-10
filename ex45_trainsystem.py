import math
class Station(object):
	
	def __init__(self, name, distance):
		self.name = name
		self.distance = distance
		self.lines = []
		self.isChangeStation = False

	def add_line(self, line):
		self.lines.append(line)
	
	def show_lines(self):
		for line in self.lines:
			print line + " ",
		print "\n"
	
	def get_lines(self):
		return self.lines

	def set_change_station(self):
		self.isChangeStation = True


class TrainLine(object):
			
	def __init__(self, name, avg_speed):
		self.name = name
		self.avg_speed = avg_speed
		self.line = []

	def create_line(self, line):
		self.line.extend(line)
		for station in self.line:
			station.add_line(self.name)

	def add_station(self, station):
		self.line.append(station)
		station.add_line(self.name)	
	
	def show_stations(self):
		print self.name + " Line: ",
		for station in self.line:
			print station.name + "(%d)" % station.distance,
		print "\n"	

	def get_change_stations(self):
		change_stations = []
		for station in self.line:
			if station.isChangeStation:
				print station.name + "(%d)" % station.distance,
				change_stations.append(station)
		return change_stations	
	
	def get_stations(self):
		return self.line

	def get_single_line_path(self, stationA, stationB):
		direction = 0
		stationA_pos = -1
		stationB_pos = -1
		for station in self.line:
			if station.name == stationA.name:
				if stationB_pos == -1:
					direction = 1
				stationA_pos = self.line.index(station)
			elif station.name == stationB.name:
				if stationA_pos == -1:
					direction  = -1
				stationB_pos = self.line.index(station)
		line = self.line[stationA_pos : stationB_pos + 1 : direction]
		distance = math.fabs( stationB.distance - stationA.distance )
		path = Path()
		path.set_path(line, distance, self.avg_speed)
		return path

class TrainNetwork(object):
	
	def __init__(self, name):
		self.name = name
		self.trainlines = []

	def get_name(self):
		return self.name

	def build_network(self, lines):
		self.trainlines = []
		self.trainlines.extend(lines)

	def get_line(self, line_name):
		for line in self.trainlines:
			if line.name == line_name:
				return line
		return None

	def show_lines(self):
		print "Displaying Network: %s" % self.name
		for line in self.trainlines:
			line.show_stations()

	def get_station(self, stationName):
		stationExists = False
		for line in self.trainlines:
			for station in line.get_stations():
				if station.name == stationName:
					stationExists = True;
					print station.name + " is on line(s): " + ", ".join(line for line in station.get_lines()) + "."
					return (stationExists, station)
		print stationName + " does not exist in this network."
		return (stationExists, None)
	
	def get_common_line(self, stationA, stationB):
		line = None
		for line1 in stationA.get_lines():
			for line2 in stationB.get_lines():
				if line1 == line2:
					line = self.get_line(line1)
					break
		return line			

	def get_common_station(self, stationA, stationB):
		commonStation = None
		for lineA in stationA.get_lines():
			for station in self.get_line(lineA).line:
				if station.isChangeStation:
					for changeLine in station.get_lines():
						for lineB in stationB.get_lines():
							if changeLine == lineB:
								commonStation = station
								line1 = lineA
								line2 = lineB
		return commonStation, lineA, lineB			

	def get_trip(self, stationA_name, stationB_name):
		stationA_exists, stationA = self.get_station(stationA_name)
		stationB_exists, stationB = self.get_station(stationB_name)
		if not (stationA_exists and stationB_exists):
			print stationA_name + " does not exist. There is no path."
			return None
		else:
			#check if the stations are on the same line	
			commonLine = self.get_common_line(stationA, stationB)
			if commonLine != None:
				path = commonLine.get_single_line_path(stationA, stationB)
				print "Speed: %.2f, Distance = %d" % ( commonLine.avg_speed, path.distance)
				path.display()

			else:
				path = self.get_multi_line_path(stationA, stationB)
				path.display()
				
	def get_multi_line_path(self, stationA, stationB):
		path = None
		distance = -1.00
		commonStation, line1, line2 = self.get_common_station(stationA, stationB)	
		if commonStation != None:
			path1 = self.get_line(line1).get_single_line_path(stationA, commonStation)	
			path2 = self.get_line(line2).get_single_line_path(commonStation, stationB)
			path1.increment_path(path2.path, path2.distance, path2.time)
		return path1

class Path(object):
	
	def __init__(self):
		self.path = []
		self.distance = 0
		self.time = 0
	#pass a path as a list of stations and extend the current path
	def set_path(self, path, distance, speed):
		self.path.extend(path)
		time = distance / speed * 60
		self.add_distance(distance)
		self.add_time(time)

	def increment_path(self, path, distance, time):
		self.path.extend(path)
		self.add_distance(distance)
		self.add_time(time)

	def add_distance(self, distance):
		self.distance += distance

	def add_time(self, time):
		self.time += time

	def display(self):
		i = 0
		while i != len(self.path) - 1:
			print self.path[i].name + "->",
			i += 1
		print self.path[-1].name 
		print "The path is %d km long and the journey will take %.2f minutes" % (self.distance, self.time) 
	

def is_station(line, stationName):
	if stationName in line:
		return (line[stationName], True)
	else:
		return None, False

def display_path(line, distance, speed):
	i = 0
	while i != len(line) - 1:
		print line[i].name + "->",
		i += 1
	print line[-1].name 
	time =   distance / speed * 60
	print "The path is %d km long and the journey will take %.2f minutes" % (distance, time) 

