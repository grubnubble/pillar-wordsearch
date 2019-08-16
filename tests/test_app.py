from app import *

CSV_FILE = 'input_file.txt'

def test_convert():
	expected = "UMKHULKI"
	assert convert(["U","M","K","H","U","L","K","I"]) == expected

def test_search_rows_forward_success():
	assert search_rows_forward('SCOTTY', CSV_FILE) == {'SCOTTY': True}