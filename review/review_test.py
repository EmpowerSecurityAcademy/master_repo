import unittest
from review import * 

class TestReview(unittest.TestCase):

	def test_construct_zoo(self):
		dictionary_list = [
							{"bird": "seagul", 
							 "dog": "labradoodle"},
							{"fish": "salmon"},
							{"snake": "anaconda"},
						  ]
		result = construct_zoo(dictionary_list)
		self.assertEqual(result, {"bird": "seagul", "dog": "labradoodle", "fish": "salmon", "snake": "anaconda"})


	def test_extract_characters(self):
		list_strings = ["hello", "I", "am", "not", "named", "steeze"]

		result = extract_characters(list_strings)
		self.assertEqual(result, ['h', 'e', 'l', 'l', 'o', 'I', 'a', 'm', 'n', 'o', 't', 'n', 'a', 'm', 'e', 'd', 's', 't', 'e', 'e', 'z', 'e'])

	def test_is_int_or_string(self):

		result = is_int_or_string(6)
		self.assertEqual(result, "int")

		result = is_int_or_string("hello")
		self.assertEqual(result, "string")

	def test_odd_numbers(self):
		result = odd_numbers([1, 2, 4, 5, 7, 8])
		self.assertEqual(result, [1, 5, 7])	

	def test_long_words(self):

		words = ["hello", "goodbye", "check", "it", "cat", "bla"]

		result = long_words(words, 4)
		self.assertEqual(result, ["hello", "goodbye", "check"])


if __name__ == '__main__':
	unittest.main()