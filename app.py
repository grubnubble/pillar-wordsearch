import csv

def get_words(csvfile):
	with open(csvfile) as file:
		reader = csv.reader(file, delimiter=',')
		return next(reader)
