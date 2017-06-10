from nose.tools import *
from ex49 import lexicon

def test_peek():
	input_string = "bear princess eat jump"
	word_list = lexicon.scan(input_string)	
	peek_words = []
	i = 0
	while i < len(word_list) + 1:
		peek_words.append(lexicon.peek(word_list[i::]))
		i += 1		
	
	assert_equal(peek_words[0], 'noun')
	assert_equal(peek_words[1], 'noun')
	assert_equal(peek_words[2], 'verb')
	assert_equal(peek_words[3], 'error')	
	assert_equal(peek_words[4], None)

def test_match():
	input_string = "bear kill princess stop door"
	word_list = lexicon.scan(input_string)
	match_words = []

	assert_equal(lexicon.match(word_list, 'noun'), ('noun', 'bear'))
	assert_equal(lexicon.match(word_list, 'verb'), ('verb', 'kill'))
	assert_equal(lexicon.match(word_list, 'noun'), ('noun', 'princess'))
	assert_equal(lexicon.match(word_list, 'verb'), ('verb', 'stop'))
	assert_equal(lexicon.match(word_list, 'noun'), ('noun', 'door'))

	assert_equal(lexicon.match([('noun', 'cabinet')], 'verb'), None) 
	assert_equal(lexicon.match(word_list, 'verb'), None)

def test_skip():
	input_string = "the in from"
	word_list = lexicon.scan(input_string)

	lexicon.skip(word_list, 'stop')
	assert_equal(word_list, [])

	word_list = lexicon.scan("in at from bear jump")
	lexicon.skip(word_list, 'stop')
	assert_equal(word_list, [('noun', 'bear'), ('error', 'jump')])

@raises(lexicon.ParserError)
def test_parse_verb():
	input_string = "eat at kill bear stop door"
	word_list = lexicon.scan(input_string)

	assert_equal(lexicon.parse_verb(word_list), ('verb', 'eat'))
	assert_equal(lexicon.parse_verb(word_list), ('verb', 'kill'))
	assert_raises(lexicon.parse_verb(word_list), lexicon.ParserError)
	assert_equal(lexicon.parse_verb(word_list), ('verb', 'stop'))
	assert_raises(lexicon.parse_verb(word_list), lexicon.ParserError) 

@raises(lexicon.ParserError)
def test_parse_object():
	input_string = "princess stop the door of the cabinet"
	word_list = lexicon.scan(input_string)

	assert_equal(lexicon.parse_object(word_list), ('noun', 'princess'))
	assert_raises(lexicon.parse_object(word_list), lexicon.ParserError)
	assert_equal(lexicon.parse_object(word_list), ('noun', 'door'))
	assert_equal(lexicon.parse_object(word_list), ('noun', 'cabinet'))

@raises(lexicon.ParserError)
def test_parse_subject():
	input_string = "bear eat princess"
	word_list = lexicon.scan(input_string)

	assert_raises(lexicon.parse_subject(word_list, ('noun', 'player')), lexicon.ParserError)

	sentence = lexicon.parse_subject(word_list, ('noun', 'player'))
	assert_equal(sentence.subject, ('noun', 'player'))
	assert_equal(sentence.verb, ('verb', 'eat'))
	assert_equal(sentence.obj, ('noun', 'princess'))

	word_list = lexcion.scan("eat honey")
	assert_raises(lexicon.parse_subject(word_list, ('noun', 'bear')), lexicon.ParserError)

@raises(lexicon.ParserError)
def test_parse_sentence():
	word_list = lexicon.scan("bear eat honey")
	assert_raises(lexicon.parse_sentence(word_list), lexicon.ParserError)

	word_list = lexicon.scan("princess stop at the door")
	sentence = lexicon.parse_sentence(word_list)
	assert_equal(sentence.subject, ('noun', 'princess'))
	assert_equal(sentence.verb, ('verb', 'stop'))
	assert_equal(sentence.obj, ('noun', 'door'))
	
	word_list = lexicon.scan("kill bear")
	sentence = lexicon.parse_sentence(word_list)
	assert_equal(sentence.subject, ('noun', 'player'))
	assert_equal(sentence.verb, ('verb', 'kill'))
	assert_equal(sentence.obj, ('noun', 'bear'))

