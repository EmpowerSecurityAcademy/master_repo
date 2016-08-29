import unittest
from sets import * 

class TestSets(unittest.TestCase):

	def test_create_set_from_sentence(self):

		result = create_set_from_sentence("driving in the District can be a struggle driving in new york and driving in san francisco can be a struggle as well")
		self.assertEqual(result, set(['a', 'be', 'and', 'francisco', 'driving', 'District', 'struggle', 'well', 'as', 'new', 'york', 'can', 'in', 'san', 'the']))

	# def test_intersection_two_sets(self):

	# 	list_a = ["a", "b", "a", "c", "d", "j", "k", "m", "a", "b", "c"]
	# 	list_b = ["a", "f", "l", "z", "j", "w", "w", "y"]

	# 	result = intersection_two_sets(list_a, list_b)

	# 	self.assertEqual(result, ["a", "j"])

	# def test_exist_only_in_first_set(self):

	# 	set_a = set(["a", "b", "a", "c", "d", "j", "k", "m", "a", "b", "c"])
	# 	set_b = set(["a", "f", "l", "z", "j", "w", "w", "y"])

	# 	result = exist_only_in_one_set(set_a, set_b)
	# 	self.assertEqual(result, set(['c', 'b', 'd', 'f', 'k', 'm', 'l', 'w', 'y', 'z']))


	# def test_unique_elements(self):

	# 	list_a = ["green", "yellow", "blue", "orange", "purple", "grey", "black", "green"]
	# 	list_b = ["pink", "blue", "black", "yellow", "tangerine"]

	# 	result = unique_elements_list_a(list_a, list_b)
	# 	self.assertEqual(result, ['purple', 'orange', 'green', 'grey'])


	# def test_combine_sets(self):

	# 	set_1 = set(["duck", "pigeon", "goose"])
	# 	set_2 = set(["duck", "wood_pecker"])

	# 	combined = combine_sets(set_1, set_2)
	# 	self.assertEqual(combined, set(['goose', 'wood_pecker', 'pigeon', 'duck']))


if __name__ == '__main__':
	unittest.main()