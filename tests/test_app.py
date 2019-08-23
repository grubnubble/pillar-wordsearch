from app import *

CSV_FILE = 'input_file.txt'
TEST_CSV_FILE = 'tests/test_input.txt'
TEST_FAIL_CSV_FILE = 'tests/test_input_fail.txt'

def test_convert():
	expected = "UMKHULKI"
	assert convert(["U","M","K","H","U","L","K","I"]) == expected

def test_get_rows():
	expected = [
		["BONES","KHAN","KIRK","SCOTTY","SPOCK","SULU","UHURA"],
		"UMKHU", "LLSHK", "HSUPJ", "UHURA"]
	assert get_rows(TEST_CSV_FILE) == expected

def test_get_columns():
	expected = ["ULHU", "MLSH", "KSUU", "HHPR", "UKJA"]
	rows_matrix = get_rows(TEST_CSV_FILE)
	assert get_columns(rows_matrix) == expected

def test_find_words():
	expected = [{'SCOTTY': (0,5), 'KIRK': (4, 7)}]
	assert find_words(CSV_FILE) == expected

def test_search_rows_success():
	expected = {'SCOTTY': (0,5), 'KIRK': (4, 7)}
	word_list = get_rows(CSV_FILE)
	assert search_rows(word_list) == expected

def test_search_rows_fail():
	expected = {}
	word_list = get_rows(TEST_FAIL_CSV_FILE)
	assert search_rows(word_list) == expected