def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sorted_words(words):
	"""Sort the words"""
	return sorted(words)

def print_first_word(words):
	word = words.pop(0)
	print word

def print_last_word(words):
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	print sorted_words(words)

def print_first_and_last(sentence):
	words = break_words(sentence)
	print print_first_word(words)
	print print_last_word(words)

def print_first_and_last_sorted(sentence):
	words = sorted_sentence(sentence)
	print print_first_word(words)
	print print_last_word(words)



