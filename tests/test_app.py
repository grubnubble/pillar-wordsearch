from app import *

CSV_FILE = 'input_file.txt'
TEST_CSV_FILE = 'tests/test_input.txt'
TEST_FAIL_CSV_FILE = 'tests/test_input_fail.txt'

def test_convert():
	expected = "UMKHULKI"
	assert convert(["U","M","K","H","U","L","K","I"]) == expected

def test_get_word_search():
	expected = [
		["BONES","KHAN","KIRK","SCOTTY","SPOCK","SULU","UHURA"],
		"UMKHU", "LLSHK", "HSUPJ", "UHURA"]
	assert get_word_search(TEST_CSV_FILE) == expected

def test_get_columns():
	expected = ["ULHU", "MLSH", "KSUU", "HHPR", "UKJA"]
	word_search = get_word_search(TEST_CSV_FILE)
	# get rid of list of words to find
	word_search.pop(0)
	assert get_columns(word_search) == expected

def test_find_words():
	expected = {'SCOTTY': (0,5), 'KIRK': (4, 7), 'BONES': (0,6), 'KHAN': (5, 9)}
	assert find_words(CSV_FILE) == expected

def test_search_rows_success():
	word_search = get_word_search(CSV_FILE)
	# get rid of list of words to find
	words = word_search.pop(0)

	expected = {'SCOTTY': (0,5), 'KIRK': (4, 7)}
	assert search(word_search, words) == expected

def test_search_rows_fail():
	word_search = get_word_search(TEST_FAIL_CSV_FILE)
	# get rid of list of words to find
	words = word_search.pop(0)

	expected = {}
	assert search(word_search, words) == expected

def test_search_columns_success():
	word_search = get_word_search(CSV_FILE)
	# get rid of list of words to find
	words = word_search.pop(0)
	columns = get_columns(word_search)

	expected = {'BONES': (0,6), 'KHAN': (5, 9)}
	assert search(columns, words, "column") == expected

def test_search_columns_fail():
	word_search = get_word_search(TEST_FAIL_CSV_FILE)
	# get rid of list of words to find
	words = word_search.pop(0)
	columns = get_columns(word_search)

	expected = {}
	assert search(columns, words, "column") == expected