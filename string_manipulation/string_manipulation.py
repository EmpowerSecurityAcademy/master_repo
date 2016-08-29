#

# return a dictionary where the keys are each letter in the past in string
# and the values are the number of times the keys exists in the string
def character_counts(string):

	return_dict = {}

	for element in string:
		return_dict[element] = 0

	for key in return_dict:
		return_dict[key] = string.count(key)

	return return_dict

# this function will take a list of strings
# and will return one string that is made up
# of adding all of the other strings together
def combine_strings(strings):

	start = ""

	for element in strings:
		start += element

	return start

# this function will take in a paragraph of text
# the output will be a list of sentences
# include periods, and remove leading empty strings
def break_into_sentence(string):

	return_array = []

	modified = string.split(".")

	for sentence in modified:
		transformed = sentence + "."
		if transformed.startswith(" "):
			transformed = transformed[1:]
		return_array.append(transformed)

	remove_last = return_array.pop()
	return return_array

# use break_into_sentence to break the text paragraph 
# into sentences
# put them into a dictionary where the key is the sentence
# and the value is the number of chrachters in the string
def count_length(string):

	return_dict = {}

	sentences = break_into_sentence(string)

	for element in sentences:

		return_dict[element] = len(element)

	return return_dict





