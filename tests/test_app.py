from app import *

CSV_FILE = 'input_file.txt'
TEST_CSV_FILE = 'tests/test_input.txt'

def test_convert():
	expected = "UMKHULKI"
	assert convert(["U","M","K","H","U","L","K","I"]) == expected

def test_get_rows():
	expected = [
		["BONES","KHAN","KIRK","SCOTTY","SPOCK","SULU","UHURA"],
		"UMKHULKINVJOCWE", "LLSHKZZWZCGJUYG", "HSUPJPRJDHSBXTG"]
	assert get_rows(TEST_CSV_FILE)

def test_find_words():
	expected = [{'SCOTTY': True, 'KIRK': True}]
	assert find_words(CSV_FILE) == expected

def test_search_rows_success():
	expected = {'SCOTTY': True, 'KIRK': True}
	word_list = get_rows(CSV_FILE)
	assert search_rows(word_list) == expected

def test_search_rows_fail():
	expected = {}
	word_list = get_rows(TEST_CSV_FILE)
	assert search_rows(word_list) == expected