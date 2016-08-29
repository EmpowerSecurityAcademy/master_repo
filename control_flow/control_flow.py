# include items, range


# this function takes two inputs, a begining value and an ending value
# use the range function to populate a list with the values in between 
# the begining and ending values
def create_list_of_range(begin, end):
	return_value = []

	for num in range(begin, end):
		return_value.append(num)

	return_value.append(end)

	return return_value

# use the dictionary.items() function to extract keys, and values
def key_value_to_list(dict_input):
	return_value = []

	for key, value in dict_input.items():
		return_value.append(key)
		return_value.append(value)

	return return_value

# use an if else block to sort dictionary values into arrays based on their value
# values in the dict_input will be san_francisco, new_york, and washington_dc
# return the three arrays in the order 1. san_francisco  2. new_york 3. washington_dc
def sort_dictionary_values(dict_input):

	san_francisco = []
	new_york = []
	washington_dc = []

	for key, value in dict_input.items():

		print(key, value)

		if value == "san_francisco":
			san_francisco.append(key)

		if value == "new_york":
			new_york.append(key)

		if value == "washington_dc":
			washington_dc.append(key)

	return san_francisco, new_york, washington_dc




