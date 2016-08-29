import unittest
from control_flow import * 

class TestControlFlow(unittest.TestCase):

	def test_create_list_of_range(self):

		result = create_list_of_range(3, 99)
		self.assertEqual(result, [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])


	def test_key_value_to_list(self):

		test_dict = {
						"code_is": "awesome",
						"aws_is": "magic",
						"cybersecurity_is": "fascinating",
						"web_application_vulnerabilities": "frightening"
					}

		result = key_value_to_list(test_dict)
		self.assertIn("code_is", result)
		self.assertIn("awesome", result)
		self.assertIn("aws_is", result)
		self.assertIn("magic", result)
		self.assertIn("cybersecurity_is", result)
		self.assertIn("fascinating", result)
		self.assertIn("web_application_vulnerabilities", result)
		self.assertIn("frightening", result)

	def test_sort_dictionary_values(self):

		neighborhoods = {
							"cole_valley": "san_francisco",
							"haight_ashbury": "san_francisco",
							"castro": "san_francisco",
							"financial_district": "san_francisco",
							"mission": "san_francisco",
							"marina": "san_francisco",
							"harlem": "new_york",
							"east_harlem": "new_york",
							"midtown": "new_york",
							"park_slope": "new_york",
							"long_island": "new_york",
							"manhattan": "new_york",
							"dupont_circle": "new_york",
							"foggy_bottom": "new_york",
							"adams_morgan": "new_york",
							"capitol_hill": "new_york",
							"kalorama": "new_york",
							"navy_yard": "new_york",							
						}

		sf, ny, dc = sort_dictionary_values(neighborhoods)

		self.assertIn("cole_valley", sf)
		self.assertIn("haight_ashbury", sf)
		self.assertIn("castro", sf)
		self.assertIn("financial_district", sf)
		self.assertIn("mission", sf)
		self.assertIn("marina", sf)
		self.assertIn("harlem", ny)
		self.assertIn("east_harlem", ny)	
		self.assertIn("midtown", ny)
		self.assertIn("park_slope", ny)	
		self.assertIn("long_island", ny)
		self.assertIn("manhattan", ny)
		self.assertIn("dupont_circle", dc)	
		self.assertIn("foggy_bottom", dc)
		self.assertIn("adams_morgan", dc)	
		self.assertIn("capitol_hill", dc)
		self.assertIn("kalorama", dc)	
		self.assertIn("navy_yard", dc)



if __name__ == '__main__':
	unittest.main()