import csv

def find_words(csvfile):
	word_search_list = get_rows(csvfile)
	found_words = []

	# search forward rows
	found_words.append(search_rows(word_search_list))

	return found_words

def search_rows(word_search_list):
	words_to_find = word_search_list.pop(0)
	found_words = {}

	for row in word_search_list:
		for word in words_to_find:
			if word in row or word in row[::-1]:
				found_words[word] = True

	return found_words

def convert(list_of_strings):
	"""Convert a list of strings to a single string"""
	return "".join(list_of_strings)

def get_rows(csvfile):
	"""Return a list of strings that represent rows in 
		the word search grid. The first element of the list
		is a list of the words to find."""
	list_of_rows = []

	with open(csvfile) as file:
		reader = csv.reader(file, delimiter=',')
		# the first line contains the words to find
		list_of_rows.append(next(reader))

		for row in reader:
			list_of_rows.append(convert(row))

	return list_of_rows