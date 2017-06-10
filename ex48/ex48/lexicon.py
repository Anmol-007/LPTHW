
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

#input_string = raw_input('> ')
#sentence = scan(input_string)
#
#print sentence
