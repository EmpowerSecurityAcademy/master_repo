import pymongo
import json
from import_config import load_config
from pymongo import MongoClient
import unicodecsv

config = load_config()

client = MongoClient(config["database"]["connection_url"])

db = client[config['database']['database_name']]
conn = db[config['database']['collection_name']]


def write_tweets_to_csv():

	cursor = conn.find()
	file = unicodecsv.writer(open("../tmp/data.csv", "wb"))
	file.writerow(["spanish_translation"])

	for tweet in cursor:
		if tweet["spanish_translation"]:
			file.writerow([tweet["spanish_translation"]])


if __name__ == '__main__':
	write_tweets_to_csv()