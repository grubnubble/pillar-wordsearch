import csv

def search_rows_forward(word, csvfile):
	found_words = {}

	with open(csvfile) as file:
		reader = csv.reader(file, delimiter=',')

		words_to_find = next(reader)

		for row in reader:
			if word in convert(row):
				found_words[word] = True

	return found_words

def convert(array_of_strings):
	"""convert an array of strings to a single string"""
	return "".join(array_of_strings)
