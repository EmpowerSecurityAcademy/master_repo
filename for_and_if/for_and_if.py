

def if_divisable_by_three(lst):

	return_array = []

	for element in lst:
		if element % 3 == 0:
			return_array.append(element)

	return return_array

def if_element_length_is_7_or_more(lst):

	return_array = []

	for element in lst:
		if len(element) >= 7:
			return_array.append(element)

	return return_array

def unpack_list_of_list(lst):

	return_array = []

	for inner_lst in lst:
		for element in inner_lst:
			return_array.append(element)

	return return_array

def if_key_in_dictionary(dct, lst):

	return_array = []

	for element in lst:
		if element in dct:
			return_array.append(element)

	return return_array







