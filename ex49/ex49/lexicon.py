
def scan(input_string):
	sentence = []
	words = input_string.split()
	for word in words:
		word_tuple = analyze_word(word)
		sentence.append(word_tuple)
	return sentence

def analyze_word(input_word):
	word_type = ''
	
	directions = ['north', 'south', 'east', 'west', 'up', 'down', 'forward', 'back', 'left', 'right']
	verbs = ['go', 'stop', 'kill' ,'eat']
	stop_words = ['the', 'from', 'at', 'it', 'in', 'of']
	nouns = ['door', 'bear', 'princess', 'cabinet']
	
	for word in directions:
		if input_word == word:
			word_type = 'direction'
			return (word_type, word)
	for word in verbs:
		if input_word == word:
			word_type = 'verb'
			return (word_type, word)	

	for word in nouns:
		if input_word == word:
			word_type = 'noun'
			return (word_type, word)	
	for word in stop_words:
		if input_word == word:
			word_type = 'stop'
			return (word_type, word)	
	
	try:
		num = int(input_word)
	except ValueError:
		word_type = 'error'
		return (word_type, input_word)
	word_type = 'number'
	return (word_type, num)	

class ParserError(Exception):
	pass

class Sentence(object):
	
	def __init__(self, subject, verb, obj):
		#remember we get ('nouns', 'princess') tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.obj = obj[1]

def peek(word_list):
	if word_list:
		word = word_list[0]
		return word[0]
	else:
		return None

def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)

		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None

def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)

def parse_verb(word_list):
	skip(word_list, 'stop')

	if peek(word_list) == 'verb':	
		return match(word_list, 'verb')
	else:
		raise ParserError("Expected a verb next.")

def parse_object(word_list):
	skip(word_list, 'stop')
	next = peek(word_list)

	if next == 'noun':
		return match(word_list, 'noun')
	if next == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expecting a noun or direction next.")

def parse_subject(word_list, subj):
	verb = parse_verb(word_list)
	obj = parse_object(word_list)

	return Sentence(subj, verb, obj)

def parse_sentence(word_list):
	skip(word_list, 'stop')

	start = peek(word_list)

	if start == 'noun':
		subj = match(word_list, 'noun')
		return parse_subject(word_list, subj)
	elif start == 'verb':
		#assume the subject is the player then
		return parse_subject(word_list, ('noun', 'player'))
	else:
		raise ParserError("Must start with a subject, object or verb not: %s" % start)

#input_string = raw_input('> ')
#word_list = scan(input_string)
#
#word = peek(word_list)
#print "peek: %s" % word
#
#while  word_list:
#	word = match(word_list, 'noun')
#	if word:
#		print "match - word type: %s, word: %s." % (word[0], word[1])
#	else:
#		print "match - %s" % word
#while word_list:
#	verb = parse_verb(word_list)
#	#obj = parse_object(word_list)
#	if verb:
#		print "verb - %s, word - %s" % (verb[0], verb[1])
	#elif obj:
#		print "object - word type: %s, word: %s" % (obj[0], obj[1])
#
#while word_list:
#	obj = parse_object(word_list)
#	if obj:
#		print "obj - word type: %s, word: %s" % (obj[0], obj[1])	
#
#while word_list:
#	sentence = parse_sentence(word_list)
#	if sentence:
#		print "sentence- subj: %s, verb: %s, obj: %s" % (sentence.subject, sentence.verb, sentence.obj) 
