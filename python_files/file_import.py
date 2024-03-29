import json
import pandas as pd
import xmltodict

# write a function that will take a string file location
# and will return a python dictionary of the json object
# example json_import('../files/data.json')
def json_import(file_name):
	with open(file_name) as data_file:
		data = json.load(data_file)
    	return data



# csv_import takes a string file location
# use the pd.read_csv function 
# to return a data frame of the loaded csv file
def csv_import(file_name):
	data = pd.read_csv(file_name)
	return data



# # write a function that takes a string file location of a text file
# # read in each line of the text file and add it to an array
# # return the array of lines
def text_import(file_name):
	with open(file_name) as f:
		data = f.readlines()
	return data

# # write a function that takes a string location of an xml file
# # return the xml file as a python dictionary
def xml_import(file_name):



