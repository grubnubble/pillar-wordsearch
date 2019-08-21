import csv

def search_rows_forward(csvfile):
	found_words = {}

	with open(csvfile) as file:
		reader = csv.reader(file, delimiter=',')
		words_to_find = next(reader)

		for row in reader:
			for word in words_to_find:
				if word in convert(row):
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