class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_birthday = Song(["Happy birthday to you", "I don't want to be sued","So I'll stop there"])

bulls_on_parade = Song(["They'll rally around the family", "With pockets full of shells"])

happy_birthday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

jack_and_jill = Song(["Jack and Jill", "Went up the Hill", "To fetch a pail of water"])

jack_and_jill.sing_me_a_song()

christmas = ["Jingle bells, jingle bells, jingle all the way", "Oh what fun it is to ride", "On a one horse open sleigh"]

christmas_song = Song(christmas)

christmas_song.sing_me_a_song()
