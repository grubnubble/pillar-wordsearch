import csv

def find_words(csvfile):
	word_search_list = get_rows(csvfile)
	found_words = []

	# search rows, forward and backward
	found_words.append(search_rows(word_search_list))

	return found_words

def search_rows(word_search_list):
	words_to_find = word_search_list.pop(0)
	found_words = {}

	row_index = 0
	for row in word_search_list:
		for word in words_to_find:
			forward_search_index = row.find(word)
			reverse_search_index = row[::-1].find(word)

			# feels overly complicated, not pythonic
			word_index = forward_search_index if forward_search_index >= 0 else None
			# assumes the word will not exist in the wordsearch more than once
			if reverse_search_index >= 0 and word_index == None:
				# subtract 1 extra to account for 0-index offset
				word_index = len(row) - 1 - reverse_search_index

			if isinstance(word_index, int):
				found_words[word] = (word_index, row_index)
		row_index += 1
	
	return found_words

def convert(list_of_strings):
	"""Convert a list of strings to a single string"""
	return "".join(list_of_strings)

def get_rows(csvfile):
	"""Return a list of strings that represent rows in 
		the word search grid. The first element of the list
		is a list of the words to find."""
	word_search = []

	with open(csvfile) as file:
		reader = csv.reader(file, delimiter=',')
		# the first line contains the words to find
		word_search.append(next(reader))

		for row in reader:
			word_search.append(convert(row))

	return word_search

def get_columns(word_search):
	"""Return a list of strings that represent columns in
		the word search grid."""

	# we don't need the list of words to find
	word_search.pop(0)
	# get dimension of the word search grid by determining the
	# 	length of the first row
	length = len(word_search[0])

	column_matrix = []

	for i in range(length):
		column = []
		for row in word_search:
			column.append(row[i])
		column_matrix.append(convert(column))

	return column_matrix