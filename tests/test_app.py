from app import *

CSV_FILE = 'input_file.txt'

def test_convert():
	expected = "UMKHULKI"
	assert convert(["U","M","K","H","U","L","K","I"]) == expected

def test_search_rows_forward_success():
	expected = {'SCOTTY': True}
	assert search_rows_forward(CSV_FILE) == expected

def test_get_rows():
	expected = [
		["BONES","KHAN","KIRK","SCOTTY","SPOCK","SULU","UHURA"],
		"UMKHULKINVJOCWE", "LLSHKZZWZCGJUYG", "HSUPJPRJDHSBXTG"]
	assert get_rows('tests/test_input.txt')