import unittest
from tuples import * 

class TestTuples(unittest.TestCase):

	def test_access_tuple_values(self):

		tup_1 = ("spain", "germany", "argentina", "peru", "japan")
		result = access_tuple_values(tup_1)
		self.assertEqual(result, ("argentina", "peru", "japan"))

		tup_2 = ("paris", "buenos aires", "tokyo", "frieburg", "huaraz", "new york", "chicago")
		result = access_tuple_values(tup_2)
		self.assertEqual(result, ("huaraz", "new york", "chicago"))

	# def test_add_value_to_tuple(self):

	# 	tup_1 = ("odeza", "kygo")
	# 	result = add_value_to_tuple(tup_1, "lana del rey")
	# 	self.assertEqual(result, ("odeza", "kygo", "lana del rey"))

	# def test_boolean_exists(self):

	# 	list_input = ["deer valley", "park city", "vail", "crested butte", "alpine"]
	# 	tup_input = ("vail", "crested butte")

	# 	result = boolean_exists(tup_input, list_input)

	# 	self.assertEqual(result, [False, False, True, True, False])

if __name__ == '__main__':
	unittest.main()