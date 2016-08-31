from file_import import *

# use json_import within this function to load the json object
# then reformat the values associated with
# the key "food", and return as a list
# ["sandwich", "cereal", "lasagna"]
def extract_food(file_name):
	data = json_import(file_name)
	modified = [data["breakfast"]["food"], data["lunch"]["food"], data["dinner"]["food"]]
	return modified


# use json_import within this function to load the json object
# then reformat the object to look like the python dictionary
# that exists on line 16 of the test file
def reformat_meals(file_name):
	data = json_import(file_name)
	reformatted = {}

	reformatted["drink"] = [data["breakfast"]["drink"], data["lunch"]["drink"], data["dinner"]["drink"]]
	reformatted["food"] = [data["breakfast"]["food"], data["lunch"]["food"], data["dinner"]["food"]]
	return reformatted


#use csv_import within this function
#return the sum of everyones age
def age_summer(file_name):
	data = csv_import(file_name)
	total_age = 0
	for age in data["age"]:
		print total_age
		total_age = age + total_age



# use csv_import
# return an array of everyones name 
# that begins with the letter j
def first_names_starting_with_j(file_name):
	data = csv_import(file_name)
	return_array = []
	for first_name in data["first_name"]:	
		if first_name[0] == "J":
			return_array.append(first_name)
	return return_array



# read in the sentences
# replace all lower and upper case i, I with an empty string ""
def extract_i_and_I_from_text(file_name):
	data = text_import(file_name)
	return_array = []
	for line in data:
		line = line.replace("i", "")
		line = line.replace("I", "")
		print line
		return_array.append(line)
	return return_array

		
extract_i_and_I_from_text("./files/data.txt")



