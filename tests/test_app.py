from app import get_words

CSV_FILE = 'input_file.txt'

def test_get_words():
	expected = ["BONES","KHAN","KIRK","SCOTTY","SPOCK","SULU","UHURA"]
	assert get_words(CSV_FILE) == expected